from google.adk.agents import Agent
from google.adk.tools import google_search

modelo = "gemini-2.0-flash"

root_agent = Agent(
    name="search",
    model=modelo,
    description="Eresun agente buscador",
    instruction="""Eres un agente q usa herarmientas de goolge para buscar informaciones importantes para el usuario 
    usando una tool:
    - google_search"""
    tools=[],
    #output_key="boas_vindas_resultado"
)
