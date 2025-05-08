from google.adk.agents import Agent
from .instructions import get_instructons
agent_instructions = get_instructons()
root_agent = Agent(
    name="rating_agent",
    model="gemini-2.0-flash",
    description=("Agent to provide rating of the parking lot"),
    instruction=agent_instructions,
    output_key="rating",
    )
