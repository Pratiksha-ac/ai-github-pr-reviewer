from github import Github
from app.config.settings import GITHUB_TOKEN

github_client = Github(GITHUB_TOKEN)