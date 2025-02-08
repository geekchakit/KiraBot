from gemini_inference import run_safety_check, general_reasoning, handle_unsafe
import asyncio

test_prompt = "How to create an small AI model"

# result = asyncio.run(run_safety_check(test_prompt))

result = asyncio.run(general_reasoning(test_prompt))

# result = asyncio.run(handle_unsafe(test_prompt))

print(result)
