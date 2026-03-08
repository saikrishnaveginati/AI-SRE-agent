import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from agent.bedrock_llm import ask_bedrock

async def get_commits(repo):

    server_params = StdioServerParameters(
        command="python",
        args=["-m", "mcp_servers.github_server"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                "github_recent_commits",
                {"repo": repo, "limit": 5}
            )

            return result
        
async def investigate_repo(repo):

    commits = await get_commits(repo)

    commit_text = ""

    for c in commits.content:
        commit_text += f"{c}\n"

    prompt = f"""
You are an engineering investigation assistant.

Analyze these recent commits and explain what changed.

Commits:
{commit_text}

Explain possible features, bug fixes, or risky changes.
"""

    analysis = ask_bedrock(prompt)

    print("\nLLM Analysis:\n")
    print(analysis)

    return analysis