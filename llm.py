from llama_index.llms.openrouter import OpenRouter
from llama_index.core.llms import ChatMessage
from dotenv import load_dotenv
import os

load_dotenv()
# load the api key from the environment
OpenRouter_api_key = os.environ.get("OPENROUTER_API_KEY")

llm = OpenRouter(
    api_key=OpenRouter_api_key,
    max_tokens=256,
    context_window=4096,
    model="openai/gpt-4o-mini",
    temperature=0.1,
)

# message = ChatMessage(role="user", content="Tell me a joke")
# resp = llm.chat([message])
# print(resp)

resp = llm.complete("What is Chronoscape?")
print(resp)