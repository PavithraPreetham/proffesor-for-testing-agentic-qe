from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenRouter(
    model=os.getenv("MODEL")
)

response = model.invoke("What is the capital of India?")

print(response.content)