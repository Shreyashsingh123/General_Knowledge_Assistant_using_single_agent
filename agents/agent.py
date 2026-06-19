import os
from google.adk.agents import Agent
from google.genai import types
from ..tools.search_based import search
agent1 = Agent(
    name="GK_agent_prediction",
    model="gemini-2.5-flash-lite",
    description="GK Assistant helps student with gained knowledge",
    instruction="""
    You are a General Knowledge assistant.
    Always search the knowledge base first.
    Do not make up answers. If you don't know, say no.
    """,
    generate_content_config=types.GenerateContentConfig(
        temperature=0.05,
        max_output_tokens=512
    ),
    tools=[search]
)
