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
   cd mcp_with_docker

   curl -LsSf https://astral.sh/uv/install.sh | sh

   uv init

   uv venv

   .\venv\Scripts\activate

2. **Add to MCP server to Claude Desktop**
    ```json
    {
        "mcpServers": {
            "terminal_docker":{
            "command": "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe",
            "args":[
                "run",
                "-i",
                "--rm",
                "--init",
                "-e", "DOCKER_CONTAINER=true",
                "-v", "D:/Banavo/mcp/model-context-protocol/mcp_with_docker/workspace:/app/workspace",
                "mcp_with_docker:latest"
            ]
            }
        }
    }

3. **Add the Dockerfile with all the configuration**
    ```bash
    1. cd servers/terminal_server/

    2. docker build -t terminal_server_docker .

4. Open the Claude and check if it's working. If not check the MCP logs.


