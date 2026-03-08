from tools.mcp_client import call_metrics, call_github
from agent.bedrock_llm import ask_bedrock


def investigate_incident(repo):

    # Step 1: check metrics
    metrics_result = call_metrics("detect_latency_issue", {})

    metrics_text = str(metrics_result)

    print("\nMetrics Analysis:")
    print(metrics_text)

    if "High latency" not in metrics_text:
        print("\nNo incident detected.")
        return

    # Step 2: fetch commits
    commits = call_github(
    "github_recent_commits",
    {"repo": repo, "limit": 5}
    )

    print("\nRecent commits:")
    print(commits)

    # Step 3: ask LLM for RCA
    prompt = f"""
A service is experiencing high latency.

Metrics output:
{metrics_text}

Recent commits:
{commits}

Explain the most likely root cause.
"""

    analysis = ask_bedrock(prompt)

    print("\nRoot Cause Analysis:")
    print(analysis)