AI SRE Agent

Autonomous Incident Investigation using LangGraph, MCP, and Amazon Bedrock

An AI-powered Site Reliability Engineering (SRE) agent that automatically investigates production incidents by correlating metrics, logs, and code changes.

Instead of manually debugging incidents across multiple tools, the agent performs the investigation workflow autonomously and produces a structured incident report.

Architecture
User Chat Interface
        │
        ▼
LangGraph Agent Orchestrator
        │
        ▼
Planner (Decision Engine)
        │
        ▼
MCP Tool Servers
 ├ Metrics Server → Prometheus-style metrics
 ├ Logs Server → AWS CloudWatch logs
 └ GitHub Server → Recent commits
        │
        ▼
Amazon Bedrock LLM
        │
        ▼
AI Root Cause Analysis
        │
        ▼
Incident Report
Problem

Production incidents usually require engineers to manually investigate:

monitoring metrics

application logs

recent code deployments

infrastructure changes

This process is slow and requires context switching across multiple systems.

This project demonstrates how an AI agent can automate the entire investigation workflow.

What the Agent Does

When an incident occurs the agent automatically:

Detects abnormal service latency from metrics

Checks recent error logs

Inspects recent GitHub commits

Correlates signals using an LLM

Generates root cause analysis

Produces a structured incident report

Example Investigation Flow
Latency spike detected
        │
        ▼
Analyze metrics
        │
        ▼
Check CloudWatch logs
        │
        ▼
Inspect recent GitHub commits
        │
        ▼
LLM performs reasoning
        │
        ▼
Generate incident report
Example Command

Run the chat interface:

python chat_interface.py

Then type:

investigate langchain-ai/langgraph

The agent will automatically execute:

metrics → logs → github → analysis → report

Example output:

Incident Summary
Service latency spike detected.

Observed Metrics
Average latency: 0.80 seconds.

Relevant Logs
ERROR timeout connecting to database.

Recent Code Changes
Commit: optimize graph execution.

Root Cause
Recent code change introduced a slow database query.

Suggested Fix
Optimize the query and introduce caching.
Project Structure
ai-sre-agent
│
├ agent
│ ├ langgraph_agent.py
│ ├ agent_state.py
│ └ bedrock_llm.py
│
├ mcp_servers
│ ├ metrics_server.py
│ ├ logs_server.py
│ └ github_server.py
│
├ tools
│ ├ mcp_client.py
│ ├ logs_tools.py
│ └ github_tools.py
│
├ chat_interface.py
├ requirements.txt
└ README.md
Tech Stack

LangGraph
Model Context Protocol (MCP)
Amazon Bedrock
Python
GitHub API
Prometheus-style metrics
AWS CloudWatch logs

Key Features

Autonomous multi-tool AI agent orchestration

LangGraph planner for investigation workflows

MCP tool architecture for modular integrations

LLM-powered root cause analysis

Automated incident report generation

Interactive chat interface for debugging

Why This Project Matters

Modern production systems generate massive amounts of telemetry data.

AI agents can act as an intelligent layer that:

investigates incidents automatically

correlates multiple observability signals

assists engineers during debugging

This project demonstrates a prototype AI SRE assistant capable of automated incident investigation.

Future Improvements

Real-time incident triggers using CloudWatch alarms

Slack notifications for incidents

Grafana monitoring dashboards

Vector search over logs

Multi-service distributed investigation


Run the Project

Install dependencies:

pip install -r requirements.txt

Start the agent:

python chat_interface.py

Investigate a repository:

investigate langchain-ai/langgraph
