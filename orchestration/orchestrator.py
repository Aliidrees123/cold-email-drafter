from agents import Runner
from my_agents.manager_agent import manager_agent

async def run_pipeline(user_prompt: str):
    result = await Runner.run(manager_agent, user_prompt)
    return result
