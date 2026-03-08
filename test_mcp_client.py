import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server_params = StdioServerParameters(
        command="python",
        args=["-m", "mcp_servers.github_server"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                "github_recent_commits",
                {"repo": "langchain-ai/langchain", "limit": 3}
            )

            print(result)


asyncio.run(main())