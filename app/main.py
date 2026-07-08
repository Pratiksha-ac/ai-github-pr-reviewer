import asyncio

from app.agents.manager_agent import ReviewManager
from app.services.report_generator import ReportGenerator

sample_code = """
def login(username,password):

    query = "SELECT * FROM users WHERE username='" + username + "'"

    if password == "admin123":
        print("Logged In")

    return True
"""

manager = ReviewManager()


async def main():

    reviews = await manager.review(sample_code)

    report = ReportGenerator.generate(reviews)

    print(report)


if __name__ == "__main__":
    asyncio.run(main())