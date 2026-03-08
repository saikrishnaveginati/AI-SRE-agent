from mcp.server.fastmcp import FastMCP
from tools.logs_tools import fetch_recent_errors

mcp = FastMCP("logs-tools")


@mcp.tool()
def check_recent_errors():
    return fetch_recent_errors()


if __name__ == "__main__":
    mcp.run()