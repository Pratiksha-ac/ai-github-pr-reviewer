from autogen_agentchat.agents import AssistantAgent
from app.core.model import model_client

architecture_agent = AssistantAgent(
    name="ArchitectureAgent",
    model_client=model_client,
    system_message="""
You are a Senior Software Architect.

Review the code for:

- SOLID Principles
- Design Patterns
- Scalability
- Maintainability
- Separation of Concerns
- Modularity

Return concise bullet points.
"""
)