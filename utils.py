import json

def extract_json_from_string(text: str) -> dict:
    """
    Extract JSON content from a string and parse it into a Python dictionary.
    
    Args:
        text (str): Input string that may contain JSON content
        
    Returns:
        dict: Parsed JSON as dictionary if found, empty dict if no valid JSON
    """
    try:
        # Find the first '{' and last '}' to locate potential JSON content
        start = text.find('{')
        end = text.rfind('}')
        
        if start != -1 and end != -1:
            json_str = text[start:end + 1]
            return json.loads(json_str)
        return {}
        
    except json.JSONDecodeError:
        # Return empty dict if JSON parsing fails
        return {}