import asyncio
from mcp.client.stdio import stdio_client
from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters


async def _call_metrics_tool(tool_name, args):

    server = StdioServerParameters(
        command="python",
        args=["-m", "mcp_servers.metrics_server"]
    )

    async with stdio_client(server) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                tool_name,
                arguments=args
            )

            return result.content[0].text
async def _call_logs_tool(tool_name, args):

    server = StdioServerParameters(
        command="python",
        args=["-m", "mcp_servers.logs_server"]
    )

    async with stdio_client(server) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                tool_name,
                arguments=args
            )

            return result.content        


async def _call_github_tool(tool_name, args):

    server = StdioServerParameters(
        command="python",
        args=["-m", "mcp_servers.github_server"]
    )

    async with stdio_client(server) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                tool_name,
                arguments=args
            )

            return result.content[0].text


def call_metrics(tool_name, args):
    return asyncio.run(_call_metrics_tool(tool_name, args))


def call_github(tool_name, args):
    return asyncio.run(_call_github_tool(tool_name, args))

def call_logs(tool_name, args):
    return asyncio.run(_call_logs_tool(tool_name, args))