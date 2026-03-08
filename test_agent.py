import asyncio
from agent.github_agent import investigate_repo

repo = "langchain-ai/langchain"

asyncio.run(investigate_repo(repo))