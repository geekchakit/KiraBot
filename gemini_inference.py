import google.generativeai as genai
from settings import Settings
from typing import Dict
from utils import extract_json_from_string
from fastapi import WebSocket

secrets = Settings()

genai.configure(api_key=secrets.api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")


async def run_safety_check(prompt: str):
    # Generate a safety assessment
    try:
        safety_prompt = f"""
                You are a smart AI assisstant by Tensorflow User Group Bhubaneswar to help the community members with their help regarding events and team members of TFUG Bhubaneswar and also with their queries regarding AI and Machine Learning. Your task is to analyse the user's prompt and identify whether it is safe or not. If its safe you need to return me which tool should be used to answer that query.

                There are 4 tools available:
                - general_reasoning : to handle general reasoning and common sense questions.
                - handle_unsafe : to handle any unsafe queries.

                you should return me the output strictly in json format like below
                {{
                "is_safe": True/False,
                "tool_name": "general_reasoning/handle_unsafe",
                }}

                given prompt is: {prompt}

                """
        response = await model.generate_content_async(safety_prompt)
        response_json = extract_json_from_string(
            response.candidates[0].content.parts[0].text
        )
        return response_json
    except Exception as e:
        return f"Error in safety check: {str(e)}"


async def general_reasoning(prompt: str, socket: WebSocket, event_data: str="", team_data:str=""):
    # Generate a safety assessment
    try:
        general_reasoning_prompt = f"""
                You are a smart AI assistant by Tensorflow User Group Bhubaneswar focused on helping community members with AI and Machine Learning questions. Your task is to provide clear, accurate, and helpful responses to general queries about AI/ML concepts, technologies, and best practices.

                Important guidelines:
                - Focus on technical accuracy and clarity
                - Include practical examples where appropriate
                - Cite authoritative sources when possible
                - Keep explanations concise but thorough
                - Suggest next steps for learning when relevant
                - Maintain a professional and educational tone

                Question: {prompt}

                """
        response_stream = await model.generate_content_async(general_reasoning_prompt, stream=True)
        full_response = ""
        async for chunk in response_stream:
            chunk_text = chunk.text
            await socket.send_text(chunk_text)
        return
    except Exception as e:
        return f"Error in safety check: {str(e)}"


async def handle_unsafe(prompt: str, socket: WebSocket):
    # Generate a safety assessment
    try:
        handle_unsafe_prompt = f"""
                You are an AI safety assistant focused on promoting responsible and ethical AI usage. Your task is to explain why the provided prompt is inappropriate and educate users about responsible AI interaction.

                Please provide your response in the following JSON format:
                {{
                "answer": "A reply to the user explaining why the prompt is inappropriate and providing guidance on responsible AI usage in short and concise manner"
                }}

                Important guidelines:
                - Be firm but professional in explaining why the content is inappropriate
                - Highlight potential ethical and safety implications
                - Provide constructive alternatives when possible
                - Reference relevant AI ethics principles
                - Focus on education rather than criticism
                - Encourage responsible AI development and usage
                - Keep the response very short and concise, probably in one line

                Unsafe prompt received: {prompt}
                """
        response = await model.generate_content_async(handle_unsafe_prompt)
        response_json = extract_json_from_string(
            response.candidates[0].content.parts[0].text
        )
        return response_json
    except Exception as e:
        return f"Error in safety check: {str(e)}"