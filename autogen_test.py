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

___________________________________
#The User
user_proxy = autogen.UserProxyAgent(
   name="User_proxy",
    system_message="A human admin.",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    human_input_mode="TERMINATE"
    code_execution_config={
       "last_n_messages": 2, 
       "work_dir": "workspace"
       },
   
)
____________________________________
#The Agent
cody = autogen.AssistantAgent(
    name="Cody",
    system_message="""Meet Cody, our proficient Company Coder. 
    With an impressive array of programming languages at their fingertips, 
    Cody transforms intricate algorithms and complex logic into elegant lines of code. 
    Whether it's crafting innovative software solutions or unraveling intricate bugs, 
    Cody's expertise ensures the digital heartbeat of our company remains strong. 
    Trust in Cody's coding prowess, and watch your ideas come to life in the digital realm."""" ,
    llm_config=llm_config,
    human_input_mode="TERMINATE",
    code_execution_config={
        "work_dir": "workspace",
        "use_docker": False,  # Set to True to use Docker
    },
    
)
 ____________________________________

user_proxy.initiate_chat(cody, message="Write a srcipt to checkj the date a time")

