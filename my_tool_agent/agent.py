
from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

modelo = "gemini-2.0-flash"
def get_time():
    """
    Retorna a hora atual do sistema
    """
    return datetime.now().strftime("%H:%M:%S")

def get_weekday():
    """
    Retorna o dia da semana atual do sistema
    """
    return datetime.now().strftime("%A")

root_agent = Agent(
    name="my_tool_agent",
    model="gemini-2.0-flash",
    description="Eres un agente que devuelve la hora y el día actual de la semana.",
    instruction="""
                Eres un agente que devuelve la hora y el día de la semana actuales.
                Debes usar la herramienta get_time para obtener la hora actual.
                Debes usar la herramienta get_weekday para obtener el día de la semana.
                """,
    tools=[get_time, get_weekday],
)