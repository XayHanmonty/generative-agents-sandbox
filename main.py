import os 
from langchain import chat_models
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
response = llm.predict("Say Hello World!")
print(response)