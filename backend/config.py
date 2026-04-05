import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "Agentic ChatGPT"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

settings = Settings()
