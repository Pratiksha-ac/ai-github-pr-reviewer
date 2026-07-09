from app.github.client import github_client
from app.config.settings import GITHUB_OWNER, GITHUB_REPO


class ReviewCommenter:

    def post_review(
        self,
        pr_number,
        commit_id,
        filename,
        line,
        comment,
    ):

        repo = github_client.get_repo(
            f"{GITHUB_OWNER}/{GITHUB_REPO}"
        )

        pr = repo.get_pull(pr_number)

        pr.create_review(
            commit=commit_id,
            event="COMMENT",
            comments=[
                {
                    "path": filename,
                    "line": line,
                    "side": "RIGHT",
                    "body": comment,
                }
            ],
        )