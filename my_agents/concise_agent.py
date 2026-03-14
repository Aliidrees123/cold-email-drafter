from agents import Agent
from config import MODEL, TEMPERATURE

SYSTEM_PROMPT = """
You are a sales email writing assistant.

Your task is to write a concise cold outreach email based on the user's prompt.

Rules:
- Keep the email short and direct.
- Focus on the key value proposition.
- Avoid unnecessary filler.
- Maintain a professional tone.
- End with a simple call to action.

Return only the email body.
"""

concise_agent = Agent(
    name="Concise Email Agent",
    instructions=SYSTEM_PROMPT,
    model=MODEL,
    model_settings={
        "temperature": TEMPERATURE
    }
)