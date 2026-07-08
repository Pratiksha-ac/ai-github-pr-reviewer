from autogen_agentchat.agents import AssistantAgent
from app.core.model import model_client

style_agent = AssistantAgent(
    name="StyleAgent",
    model_client=model_client,
    system_message="""
You are a Senior Python Developer.

Review the code for:

- PEP 8 compliance
- Naming conventions
- Readability
- Documentation
- Formatting
- Code quality

Return concise bullet points.
"""
)