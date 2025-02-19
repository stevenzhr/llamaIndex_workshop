import os
from dotenv import load_dotenv

from llama_index.llms.openrouter import OpenRouter
from llama_index.core.llms import ChatMessage


load_dotenv()
# load the api key from the environment
OpenRouter_api_key = os.environ.get("OPENROUTER_API_KEY")

# Create an OpenRouter LLM
llm = OpenRouter(
    # TODO: add llm config here
)

# # Call complete with prompt
# resp = TODO: call complete with prompt
# print(resp)

# # Call chat with ChatMessage List
# message = TODO: create a ChatMessage object
# resp = TODO: call chat with ChatMessage List
# print(resp)
