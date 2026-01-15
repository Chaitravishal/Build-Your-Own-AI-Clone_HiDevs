from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os

# The API key will be loaded automatically from .env file by load_dotenv()

chat = ChatOpenAI()

response = chat.invoke([HumanMessage(content="Hello, are you working?")])

# Print the response
print(response.content)