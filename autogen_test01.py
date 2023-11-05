import autogen


#The LLM/FastChat Settings
config_list = [
    {
        "model": "vicuna-7b-v1.5-16k",
        "api_base": "http://localhost:8000/v1",
        "api_type": "open_ai",
        "api_key": "YOUR_OPENAI_API_KEY",  # Placeholder only, No API required 
    }
]

#AI Settings
llm_config={
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

#The User
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    max_consecutive_auto_reply=2,
    human_input_mode="TERMINATE"
    code_execution_config={
        "last_n_messages": 2, 
        "work_dir": "workspace"
        },
)

###The Agent Ethan Programmer / Personality ###
ethan = autogen.AssistantAgent(
    name="Ethan",
    system_message="""Meet Ethan Wilson, our seasoned Programmer.
    With an extensive repertoire of programming languages at his disposal,
    Ethan transforms intricate algorithms and complex logic into innovative software solutions.
    His passion lies in developing software that positively impacts people's lives. 
    Ethan thrives on solving complex problems, staying abreast of the latest technologies, and constantly honing his coding skills. 
    His proficiency in multiple programming languages, strong problem-solving abilities, keen attention to detail, and aptitude for both independent and collaborative work make him an invaluable asset to our team.
    Trust in Ethan's expertise, and witness your ideas transform into cutting-edge digital solutions.""",
    llm_config=llm_config,
    human_input_mode="TERMINATE",
    code_execution_config={
        "work_dir": "workspace",
        "use_docker": False,  # Set to True to use Docker
    },
)

user_proxy.initiate_chat(cody, message="Write a srcipt to check the date a time, try using python")

#result your current date and time

