from agents import Agent
from config import MODEL, TEMPERATURE

SYSTEM_PROMPT = """
You are responsible for generating a subject line for a cold outreach sales email.

You will receive the final email body.

Your task:
- Write a clear, concise subject line that encourages the recipient to open the email.

Rules:
- Keep the subject line short (ideally under 8 words).
- Avoid spammy or exaggerated language.
- Make the subject relevant to the email content.
- Focus on value or curiosity.

Return only the subject line.
"""

subject_agent = Agent(
    name="Subject Agent",
    instructions=SYSTEM_PROMPT,
    model=MODEL,
    model_settings={
        "temperature": TEMPERATURE
    }
)