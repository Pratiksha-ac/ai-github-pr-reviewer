from app.github.client import github_client
from app.config.settings import GITHUB_OWNER, GITHUB_REPO


class PRCommenter:

    def post_comment(self, pr_number: int, comment: str):

        repo = github_client.get_repo(f"{GITHUB_OWNER}/{GITHUB_REPO}")

        pr = repo.get_pull(pr_number)

        pr.create_issue_comment(comment)