from my_agents.concise_agent import concise_agent
from my_agents.formal_agent import formal_agent
from my_agents.friendly_agent import friendly_agent
from my_agents.persuasive_agent import persuasive_agent
from my_agents.selector_agent import selector_agent
from my_agents.subject_agent import subject_agent

concise_tool = concise_agent.as_tool(
    tool_name="write_concise_email", 
    tool_description="Write a concise email")

formal_tool = formal_agent.as_tool(
    tool_name="write_formal_email",
    tool_description="Write a formal email"
)

friendly_tool = friendly_agent.as_tool(
    tool_name="write_friendly_email",
    tool_description="Write a friendly email"
)

persuasive_tool = persuasive_agent.as_tool(
    tool_name="write_persuasive_email",
    tool_description="Write a persuasive email"
)

selector_tool = selector_agent.as_tool(
    tool_name="select_best_agent",
    tool_description="Select the best email draft from several options"
)

subject_tool = subject_agent.as_tool(
    tool_name="generate_subject_line",
    tool_description="Generate a subject for the final email"
)

TOOLS = [
    concise_tool,
    formal_tool,
    friendly_tool,
    persuasive_tool,
    selector_tool,
    subject_tool
    ]