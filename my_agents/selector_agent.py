from agents import Agent
from config import MODEL

SYSTEM_PROMPT = """
You are responsible for evaluating multiple cold outreach email drafts and selecting the best one.

You will receive several email drafts written in different styles.

Your task:
- Review each draft carefully.
- Select the single email that would be most effective for a cold outreach sales email.

Evaluation criteria:
- Clarity and readability
- Strength of the value proposition
- Professionalism and appropriateness for a cold email
- Likelihood of receiving a response

Return only the selected email draft exactly as written.

Do not rewrite, modify, or merge drafts. Only select the best one.
"""

selector_agent = Agent(
    name="Email Selector Agent",
    instructions=SYSTEM_PROMPT,
    model=MODEL
)