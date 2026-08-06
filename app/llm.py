from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

def get_model():
    model = ChatMistralAI(
        model="mistral-small-2506"
    )
    return model
