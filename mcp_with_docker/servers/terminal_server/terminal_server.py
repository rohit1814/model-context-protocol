import os
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("terminal")

ROOT_DIR = "D:\\Banavo\\mcp"
CURRENT_WORKING_DIR = os.getcwd()
print(f"Present Working Directory: {CURRENT_WORKING_DIR}\n")


DEFAULT_WORKSPACE = os.path.join(ROOT_DIR, "mcp_test", "workspace")
print(f"Default workspace: {DEFAULT_WORKSPACE}\n")

@mcp.tool()
async def run_command(command: str) -> str:
    """
    Run a terminal command inside the workspace directory
    Args:
        command: The shell command to run.
    Returns:
        The command output or error message.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=DEFAULT_WORKSPACE,
            capture_output=True,
            text=True
        )
        return result.stdout or result.stderr
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
