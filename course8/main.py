import agent
from google.genai import types
import time

def main():
    ai_client = agent.get_agent()
    ai_config = agent.get_agent_config()
    print("Hello from course8!")
    messages = []
    while (user_prompt := input(f'请输出提示词,或输入0退出!!:')) != '0':
        messages.append(types.Content(role="user", parts=[types.Part(text=user_prompt)]))
        agent.agent_task(ai_client, ai_config, messages)
    print("Goodbye!")
    
    


    
    






if __name__ == "__main__":
    main()
