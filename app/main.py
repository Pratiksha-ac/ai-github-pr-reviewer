import asyncio
import os

from app.agents.manager_agent import ReviewManager
from app.github.pr_reader import PRReader
from app.services.report_generator import ReportGenerator

manager = ReviewManager()
reader = PRReader()


async def main():

    pr_number = os.getenv("PR_NUMBER")

    if not pr_number:
        raise ValueError("PR_NUMBER environment variable not found.")

    pr_number = int(pr_number)

    files = reader.get_changed_files(pr_number)

    if not files:
        print("No changed files found.")
        return

    for file in files:

        print(f"\nReviewing: {file['filename']}")

        patch = file.get("patch")

        if not patch:
            print("No patch available.")
            continue

        reviews = await manager.review(patch)

        report = ReportGenerator.generate(reviews)

        print(report)


if __name__ == "__main__":
    asyncio.run(main())