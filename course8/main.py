import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import prompts
import call_function

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
    ai_config = types.GenerateContentConfig(system_instruction=prompts.system_prompt, tools=[call_function.available_functions])
    result_content = client.models.generate_content(model='gemini-2.5-flash',
                                    contents=messages, config=ai_config)
    

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
    if result_content.function_calls:
        for i in result_content.function_calls:
            print(f"Calling function: {i.name}({i.args})")
            function_result = call_function.call_function(i, args.verbose)
            if not function_result.parts or not function_result.parts[0]:
                raise Exception('parts is null')
            function_response = function_result.parts[0].function_response
            if not function_response:
                raise Exception('Response is null')
            if args.verbose:
                print(f"-> {function_result.parts[0].function_response.response}")

if __name__ == "__main__":
    main()
