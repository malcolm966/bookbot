import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import prompts
import call_function
import time

def get_agent() -> genai.Client:
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("Can't Find GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    return client

def get_agent_config():
    ai_config = types.GenerateContentConfig(system_instruction=prompts.system_prompt, tools=[call_function.available_functions])
    return ai_config

def agent_task(client:genai.Client, config:types.GenerateContentConfigOrDict ,messages:list):

    for _ in range(20):
        result_content = client.models.generate_content(model='gemini-2.5-flash',
                                        contents=messages, config=config)

        usage_metadata = result_content.usage_metadata
        if not usage_metadata:
            raise RuntimeError('This is a failed API request!')

        # Add all candidates to the conversation history
        result_candidates = result_content.candidates
        if result_candidates:
            for candidate in result_candidates:
                if candidate.content:
                    messages.append(candidate.content)

        # Check if the model requested function calls
        if result_content.function_calls:
            # Collect all function results
            function_results = []
            for func_call in result_content.function_calls:
                print(f" - Calling function: {func_call.name}")
                function_result = call_function.call_function(func_call)
                if not function_result.parts or not function_result.parts[0]:
                    raise Exception('parts is null')
                function_results.extend(function_result.parts)

            # Add function results to messages with role="user"
            messages.append(types.Content(role="user", parts=function_results))
        else:
            # No function calls - model has a final response
            if result_content.text:
                print("Final response:")
                print(result_content.text)
            return
        time.sleep(3.5)

    # If we reach here, max iterations exceeded
    print("Error: Maximum iterations (20) reached without a final response from the model.")
    exit(1)
    
    


