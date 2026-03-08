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

## Quick Start

### 1. Clone the repository


git clone https://github.com/YOUR_USERNAME/AI-SRE-agent.git

cd AI-SRE-agent


### 2. Install dependencies


pip install -r requirements.txt


### 3. Run the agent


python chat_interface.py


### 4. Start an investigation

Example query:


investigate langchain-ai/langgraph


The agent will automatically run the investigation workflow and generate an **incident report**.

---

## Future Improvements

Planned enhancements include:

- Real-time incident triggers using monitoring alerts  
- Slack incident notifications  
- Grafana dashboard integration  
- Vector-based log retrieval  
- Multi-service investigation across distributed systems  
- Kubernetes observability support  

---

## Author

**Sai Krishna Veginati**

Machine Learning Engineer focused on **AI systems, agent orchestration, and production-scale ML infrastructure.**
