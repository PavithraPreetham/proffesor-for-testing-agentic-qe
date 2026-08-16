import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_BASE_URL="https://openrouter.ai/api"

def get_client():
    return anthropic.Anthropic(auth_token=os.getenv("OPENROUTER_API_KEY"), base_url=OPENROUTER_BASE_URL)