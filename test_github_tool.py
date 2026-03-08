from tools.github_tools import get_recent_commits


repo = "langchain-ai/langchain"

commits = get_recent_commits(repo)

for c in commits:
    print(c)