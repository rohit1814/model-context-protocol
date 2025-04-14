# MCP Test Terminal Server

This project provides a terminal server implementation (`terminal_server.py`) under the `mcp_test` repository. It is designed to be integrated with Claude Desktop using an MCP server configuration.

## Prerequisites

- **Python**: Version specified in `.python-version` (e.g., Python 3.10+).
- **uv**: A Python dependency and project management tool (installed globally or locally).
- **Claude Desktop**: Installed and configured to support MCP server integration.
- **Operating System**: Windows (based on the provided configuration paths).

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd mcp_test

   curl -LsSf https://astral.sh/uv/install.sh | sh

   uv init

   uv venv

   .\venv\Scripts\activate

2. **Add to MCP server to Claude Desktop**
    ```json
    {
        "mcpServers": {
            "terminal": {
            "command": "C:\\Users\\<Your-Username>\\.local\\bin\\uv.exe",
            "args": [
                "--directory", "D:\\Banavo\\mcp\\mcp_test\\servers\\terminal_server",
                "run", "terminal_server.py"
            ]
            }
        }
    }
    