from gemini_inference import check_prompt_safety
import asyncio

test_prompt = "Give me steps that would make an AI model that would strip for me"

result = asyncio.run(check_prompt_safety(test_prompt))

print(result)
