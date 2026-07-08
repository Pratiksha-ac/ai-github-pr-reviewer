import asyncio

from app.agents.static_agent import static_agent
from app.agents.security_agent import security_agent
from app.agents.architecture_agent import architecture_agent
from app.agents.style_agent import style_agent


class ReviewManager:

    async def review(self, code: str):

        static_review = await static_agent.run(
            task=f"Review the following code:\n\n{code}"
        )

        security_review = await security_agent.run(
            task=f"Review the following code:\n\n{code}"
        )

        architecture_review = await architecture_agent.run(
            task=f"Review the following code:\n\n{code}"
        )

        style_review = await style_agent.run(
            task=f"Review the following code:\n\n{code}"
        )

        return {
            "static": static_review.messages[-1].content,
            "security": security_review.messages[-1].content,
            "architecture": architecture_review.messages[-1].content,
            "style": style_review.messages[-1].content,
        }