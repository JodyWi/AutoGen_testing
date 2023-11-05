import autogen


#The LLM/FastChat Settings
config_list = [
    {
        "model": "vicuna-7b-v1.5-16k",
        "api_base": "http://localhost:8000/v1",
        "api_type": "open_ai",
        "api_key": "YOUR_OPENAI_API_KEY",  # Replace with your OpenAI API key
    }
]

#AI Settings
llm_config={
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

user_proxy = autogen.UserProxyAgent(
   name="User_proxy",
   system_message="A human admin.",
   code_execution_config={"last_n_messages": 2, "work_dir": "workspace"},
   human_input_mode="TERMINATE"
)

