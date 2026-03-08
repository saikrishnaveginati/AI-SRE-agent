# AI SRE Agent (LangGraph)

## AI-Powered Incident Investigation Agent for SRE Workflows

AI agent that investigates production incidents by analyzing **metrics, logs, and code changes**, then generates a structured **root cause analysis report**.

---

![Python](https://img.shields.io/badge/Python-3.10-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent%20Orchestration-green)
![MCP](https://img.shields.io/badge/MCP-Tool%20Integration-purple)
![Amazon Bedrock](https://img.shields.io/badge/Amazon%20Bedrock-LLM-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Overview

This project explores how **AI agents can automate incident investigation workflows** typically handled by Site Reliability Engineers.

Instead of manually debugging incidents across multiple systems, the agent collects signals from observability systems, reasons across them using an LLM, and generates a structured incident report.

The system is built using **LangGraph**, which allows explicit control over multi-step reasoning workflows and shared agent state.

---

## Key Capabilities

- Automated **incident investigation workflows**
- Analysis of **metrics, logs, and recent code changes**
- Multi-step reasoning using **LangGraph state graphs**
- Tool integrations using **Model Context Protocol (MCP)**
- AI-assisted **root cause analysis**
- Structured **incident reports with remediation suggestions**

---

## Example Investigation Workflow


Latency spike detected
│
▼
Analyze service metrics
│
▼
Inspect application logs
│
▼
Check recent GitHub commits
│
▼
LLM performs reasoning
│
▼
Generate incident report


The **planner node** decides which step should execute next based on the shared agent state.

---

## Architecture Flow


User Chat Interface
│
▼
LangGraph Agent Orchestrator
│
▼
Planner (Decision Engine)
│
▼
Tool Layer (MCP Servers)
├ Metrics Server
├ Logs Server
└ GitHub Server
│
▼
Amazon Bedrock LLM
│
▼
Root Cause Analysis
│
▼
Incident Report


This architecture separates **agent orchestration, tool integrations, and reasoning models**, making the system easier to extend.

---

## Project Structure


AI-SRE-agent
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


The structure separates **agent logic, tool servers, and integrations** for easier extensibility.

---

## Tech Stack

- Python  
- LangGraph  
- Model Context Protocol (MCP)  
- Amazon Bedrock  
- GitHub API  
- AWS CloudWatch  

---

