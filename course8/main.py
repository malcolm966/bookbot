import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("Can't Find GEMINI_API_KEY")
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    print("Hello from course8!")
    client = genai.Client(api_key=api_key)
    result_content = client.models.generate_content(model='gemini-2.5-flash',
                                    contents=messages)
    

    usage_metadata = result_content.usage_metadata
    if not usage_metadata:
        raise RuntimeError('This is a failed API request!')
    X = usage_metadata.prompt_token_count
    Y = usage_metadata.candidates_token_count

    if args.verbose:
        print(f'''
            User prompt: {messages}  
            Prompt tokens: {X}
            Response tokens: {Y}
            ''')
    print(result_content.text)
 

if __name__ == "__main__":
    main()
