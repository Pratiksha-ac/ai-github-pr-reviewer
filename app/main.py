import asyncio
import os

from app.agents.manager_agent import ReviewManager
from app.github.pr_reader import PRReader
from app.github.commenter import PRCommenter
from app.services.report_generator import ReportGenerator

manager = ReviewManager()
reader = PRReader()
commenter = PRCommenter()

MAX_RETRIES = 3


async def main():

    pr_number = os.getenv("PR_NUMBER")

    if not pr_number:
        raise ValueError("PR_NUMBER environment variable not found.")

    pr_number = int(pr_number)

    files = reader.get_changed_files(pr_number)

    if not files:
        print("No changed files found.")
        return

    all_reports = []

    for file in files:

        print(f"\nReviewing: {file['filename']}")

        patch = file.get("patch")

        if not patch:
            print(f"Skipping {file['filename']} (No patch available)")
            continue

        reviews = None

        for attempt in range(MAX_RETRIES):

            try:
                reviews = await manager.review(patch)
                break

            except Exception as e:

                print(
                    f"Attempt {attempt + 1}/{MAX_RETRIES} failed for {file['filename']}"
                )

                print(e)

                if attempt == MAX_RETRIES - 1:
                    print(f"Skipping {file['filename']}")
                    reviews = {
                        "security": "❌ Review failed",
                        "architecture": "❌ Review failed",
                        "style": "❌ Review failed",
                        "static": "❌ Review failed",
                    }

                else:
                    await asyncio.sleep(5)

        report = ReportGenerator.generate(reviews)

        all_reports.append(
            {
                "filename": file["filename"],
                "report": report,
            }
        )

    final_report = "# 🤖 AI Pull Request Review\n\n"

    for item in all_reports:

        final_report += f"## 📄 {item['filename']}\n\n"

        final_report += item["report"]

        final_report += "\n\n---\n\n"

    commenter.post_comment(pr_number, final_report)

    print("✅ Review posted successfully.")


if __name__ == "__main__":
    asyncio.run(main())