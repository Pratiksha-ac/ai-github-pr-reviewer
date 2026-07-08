from app.github.client import github_client
from app.config.settings import GITHUB_OWNER, GITHUB_REPO

repo = github_client.get_repo(f"{GITHUB_OWNER}/{GITHUB_REPO}")

print("Repository Name:", repo.name)
print("Default Branch:", repo.default_branch)
print("Stars:", repo.stargazers_count)