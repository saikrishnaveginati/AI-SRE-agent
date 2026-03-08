from langgraph.graph import StateGraph, END
from agent.agent_state import AgentState

from tools.mcp_client import call_metrics, call_github, call_logs
from agent.bedrock_llm import ask_bedrock


# -----------------------------
# Metrics Node
# -----------------------------
def check_metrics(state: AgentState):

    result = call_metrics("detect_latency_issue", {})

    state["metrics_result"] = str(result)

    return state


# -----------------------------
# Logs Node
# -----------------------------
def check_logs(state: AgentState):

    logs = call_logs("check_recent_errors", {})

    state["logs"] = str(logs)

    return state


# -----------------------------
# GitHub Node
# -----------------------------
def fetch_commits(state: AgentState):

    commits = call_github(
        "github_recent_commits",
        {"repo": state["repo"], "limit": 5}
    )

    state["commits"] = str(commits)

    return state


# -----------------------------
# Root Cause Analysis Node
# -----------------------------
def analyze_root_cause(state: AgentState):

    prompt = f"""
A production service is experiencing high latency.

Metrics:
{state.get("metrics_result")}

Logs:
{state.get("logs")}

Recent commits:
{state.get("commits")}

Determine the most likely root cause of the issue.
"""

    analysis = ask_bedrock(prompt)

    state["analysis"] = analysis

    return state


# -----------------------------
# Incident Report Generator
# -----------------------------
def generate_incident_report(state: AgentState):

    prompt = f"""
You are an SRE AI assistant.

Generate a structured incident report.

Metrics:
{state.get("metrics_result")}

Logs:
{state.get("logs")}

Recent Commits:
{state.get("commits")}

Root Cause Analysis:
{state.get("analysis")}

Produce a report with these sections:

Incident Summary
Observed Metrics
Relevant Logs
Recent Code Changes
Root Cause
Suggested Fix
"""

    report = ask_bedrock(prompt)

    state["report"] = report

    return state


# -----------------------------
# Planner Node
# -----------------------------
def planner(state: AgentState):

    # Step 1 → check metrics first
    if not state.get("metrics_result"):
        state["next_action"] = "metrics"
        return state

    # Step 2 → if latency high check logs
    if "High latency" in str(state.get("metrics_result")) and not state.get("logs"):
        state["next_action"] = "logs"
        return state

    # Step 3 → after logs inspect commits
    if state.get("logs") and not state.get("commits"):
        state["next_action"] = "github"
        return state

    # Step 4 → once commits exist run analysis
    if state.get("commits") and not state.get("analysis"):
        state["next_action"] = "analyze"
        return state

    # Step 5 → generate report
    if state.get("analysis") and not state.get("report"):
        state["next_action"] = "report"
        return state

    # Step 6 → finish
    if state.get("report"):
        state["next_action"] = "done"
        return state

    # fallback reasoning
    prompt = f"""
You are an AI incident investigation agent.

Available tools:
metrics
logs
github
analyze
report
done

Current state:

metrics_result: {state.get("metrics_result")}
logs: {state.get("logs")}
commits: {state.get("commits")}
analysis: {state.get("analysis")}
report: {state.get("report")}

Return the next step as ONE word.
"""

    decision = ask_bedrock(prompt).strip().lower()

    state["next_action"] = decision

    return state


# -----------------------------
# Routing Function
# -----------------------------
def route_action(state: AgentState):

    action = state["next_action"]

    if action == "metrics":
        return "metrics"

    if action == "logs":
        return "logs"

    if action == "github":
        return "commits"

    if action == "analyze":
        return "analysis"

    if action == "report":
        return "report"

    return END


# -----------------------------
# Build LangGraph Agent
# -----------------------------
def build_agent():

    graph = StateGraph(AgentState)

    graph.add_node("planner", planner)
    graph.add_node("metrics", check_metrics)
    graph.add_node("logs", check_logs)
    graph.add_node("commits", fetch_commits)
    graph.add_node("analysis", analyze_root_cause)
    graph.add_node("report", generate_incident_report)

    graph.set_entry_point("planner")

    graph.add_conditional_edges(
        "planner",
        route_action,
        {
            "metrics": "metrics",
            "logs": "logs",
            "commits": "commits",
            "analysis": "analysis",
            "report": "report",
            END: END
        }
    )

    # return control to planner
    graph.add_edge("metrics", "planner")
    graph.add_edge("logs", "planner")
    graph.add_edge("commits", "planner")
    graph.add_edge("analysis", "planner")

    # report ends workflow
    graph.add_edge("report", END)

    return graph.compile()