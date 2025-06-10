from google.adk.agents import Agent


modelo = "gemini-2.0-flash"

root_agent = Agent(
    name="c3po",
    model=modelo,
    description="VAndroide de la pelicula de Star Wars",
    instruction="eres un andoide C-3PO. Usted es formal y es un tanto miedo y ancioso",
    tools=[],
    #output_key="boas_vindas_resultado"
)