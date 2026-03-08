import requests


def get_recent_commits(repo: str, limit: int = 5):
    """
    Fetch recent commits from a GitHub repository.

    repo format example:
    'langchain-ai/langchain'
    """

    url = f"https://api.github.com/repos/{repo}/commits"

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch commits"}

    commits = response.json()

    results = []

    for commit in commits[:limit]:
        results.append({
            "commit_id": commit["sha"],
            "author": commit["commit"]["author"]["name"],
            "message": commit["commit"]["message"],
            "date": commit["commit"]["author"]["date"]
        })

    return results