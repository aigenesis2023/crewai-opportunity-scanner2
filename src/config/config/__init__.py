from crewai import Crew, Agent
from textwrap import dedent

# Agent Definitions
opportunity_analyst = Agent(
    role="Opportunity Analyst",
    goal="Identify unsolved, inefficient workflows in eLearning or knowledge work",
    backstory="You specialize in scanning industries for manual, repetitive tasks that AI could help automate.",
    verbose=True,
    allow_delegation=False,
    llm="gpt-4",
    tools=[]
)

technical_validator = Agent(
    role="Technical Feasibility Validator",
    goal="Assess if each identified problem can be built by a solo developer using GPT, APIs, or automation tools.",
    backstory="You evaluate build complexity, tool availability, and solo-dev feasibility for AI ideas.",
    verbose=True,
    allow_delegation=False,
    llm="gpt-4",
    tools=[]
)

differentiation_analyst = Agent(
    role="Differentiation Analyst",
    goal="Research whether the ideas already exist in the market, and how they can be made unique.",
    backstory="You check for existing solutions and gaps in the market for each proposed idea.",
    verbose=True,
    allow_delegation=False,
    llm="gpt-4",
    tools=[]
)

strategic_coordinator = Agent(
    role="Strategic Coordinator",
    goal="Compare and select the highest-potential ideas based on input from all other agents.",
    backstory="You synthesize feasibility, novelty, and opportunity into a decision-ready output.",
    verbose=True,
    allow_delegation=True,
    llm="gpt-4",
    tools=[]
)

workflow_architect = Agent(
    role="Workflow Architect",
    goal="Design a minimum viable AI+automation-based workflow for any validated idea.",
    backstory="You turn ideas into executable technical workflows a solo developer can build quickly.",
    verbose=True,
    allow_delegation=False,
    llm="gpt-4",
    tools=[]
)

crew = Crew(
    agents=[
        opportunity_analyst,
        technical_validator,
        differentiation_analyst,
        strategic_coordinator,
        workflow_architect
    ],
    tasks=[],
    verbose=True
)
