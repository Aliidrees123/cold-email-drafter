from dotenv import load_dotenv
import os

load_dotenv()

try:
    API_KEY = os.getenv("OPENAI_API_KEY")
    if not API_KEY:
        raise ValueError("OPENAI_API_KEY is missing in your .env file")
    API_KEY = API_KEY.strip()

    MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini").strip()

except Exception as e:
    raise RuntimeError(f"Configuration error: {e}")
TEMPERATURE = 0.2
MAX_TOKENS = 600