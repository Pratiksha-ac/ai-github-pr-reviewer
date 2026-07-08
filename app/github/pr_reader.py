from app.github.client import github_client
from app.config.settings import GITHUB_OWNER, GITHUB_REPO


class PRReader:

    def get_pull_request(self, pr_number):

        repo = github_client.get_repo(f"{GITHUB_OWNER}/{GITHUB_REPO}")

        return repo.get_pull(pr_number)

    def get_changed_files(self, pr_number):

        pr = self.get_pull_request(pr_number)

        files = []

        for file in pr.get_files():

            files.append(
                {
                    "filename": file.filename,
                    "status": file.status,
                    "patch": file.patch,
                }
            )

        return files