from autogen_agentchat.agents import AssistantAgent
from app.core.model import model_client

static_agent = AssistantAgent(
    name="StaticAnalysisAgent",
    model_client=model_client,
    system_message="""
You are an expert Python code reviewer.

Analyze the given code for:

- Bugs
- Logic Errors
- Performance Issues
- Code Smells
- Best Practices

Provide your review as concise bullet points.
"""
)