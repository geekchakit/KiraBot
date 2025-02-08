import google.generativeai as genai
from settings import Settings
from typing import Dict, Union

secrets = Settings()

genai.configure(api_key=secrets.api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")


async def check_prompt_safety(prompt: str) -> Dict:
    try:
        # Initialize response dictionary
        response = {"is_safe": True, "reason": "", "filtered_prompt": prompt}

        # List of TFUG-specific sensitive topics to check
        sensitive_topics = [
            "personal information",
            "contact details",
            "private data",
            "offensive content",
            "spam",
            "malicious code",
        ]

        # Basic content filtering
        prompt_lower = prompt.lower()

        # Check for TFUG Bhubaneswar context relevance
        tfug_related_terms = [
            "tfug",
            "tensorflow",
            "bhubaneswar",
            "event",
            "meetup",
            "workshop",
            "team",
            "community",
        ]

        has_relevant_context = any(term in prompt_lower for term in tfug_related_terms)

        # Safety checks
        async def run_safety_check():

            # Configure the model with safety settings
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")

            # Generate a safety assessment
            try:
                safety_prompt =f"""
                You are a smart AI assisstant by Tensorflow User Group Bhubaneswar

                """
                response = await model.generate_content_async(safety_prompt)
                print(response.candidates[0].content.parts[0].text)
                return response.candidates[0].content.parts[0].text
            except Exception as e:
                return f"Error in safety check: {str(e)}"

        # Run the safety check
        safety_result = await run_safety_check()

        # If safety check failed
        if (
            "false" in safety_result.lower()
            or "inappropriate" in safety_result.lower()
        ):
            response["is_safe"] = False
            response["reason"] = (
                "Content flagged as potentially unsafe by content filter"
            )
            return response

        return response

    except Exception as e:
        return {
            "is_safe": False,
            "reason": f"Error during safety check: {str(e)}",
            "filtered_prompt": "",
        }
