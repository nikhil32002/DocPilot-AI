import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

print("API KEY:", os.getenv("GROQ_API_KEY"))
print("MODEL:", os.getenv("MODEL_NAME"))

class GroqService:

    def __init__(self):
        self.llm = ChatGroq(
            model=os.getenv("MODEL_NAME"),
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0.3,
        )

    def get_llm(self):
        return self.llm

groq_service = GroqService()

