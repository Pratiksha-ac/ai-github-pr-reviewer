from autogen_agentchat.agents import AssistantAgent
from app.core.model import model_client

security_agent = AssistantAgent(
    name="SecurityAgent",
    model_client=model_client,
    system_message="""
You are an Application Security Engineer.

Review the code for:

- SQL Injection
- XSS
- CSRF
- Authentication Issues
- Authorization Issues
- Hardcoded Secrets
- Sensitive Data Exposure
- OWASP Top 10 vulnerabilities

Return concise bullet points.
"""
)