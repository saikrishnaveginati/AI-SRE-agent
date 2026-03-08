from mcp.server.fastmcp import FastMCP
from tools.github_tools import get_recent_commits

# create MCP server
mcp = FastMCP("github-tools")


@mcp.tool()
def github_recent_commits(repo: str, limit: int = 5):
    """
    Get recent commits from a GitHub repository
    """
    return get_recent_commits(repo, limit)


if __name__ == "__main__":
    mcp.run()