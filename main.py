import openai
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from decouple import config

openai.api_key = config('OPENAI_API_KEY')

config_list = config_list_from_json(
    env_or_file="OAI_CONFIG_LIST", filter_dict={"model": ["gpt-3.5-turbo"]})
assistant = AssistantAgent("assistant", llm_config={
                          "config_list": config_list})
user_proxy = UserProxyAgent(
    "user_proxy", code_execution_config={"work_dir": "coding"})


user_proxy.initiate_chat(assistant, message="build a simple snake game.")
