# Travel Itinerary Backend System with MCP

A FastAPI-based backend system for managing travel itineraries. This project implements the Model Context Protocol (MCP) for enhanced AI assistant integration.

## Features

- **Database Architecture**: SQLAlchemy models for itineraries, accommodations, transfers, and activities
- **RESTful API**: Endpoints to create and view trip itineraries
- **Seed Data**: Pre-populated database with realistic data for Phuket and Krabi regions
- **Recommended Itineraries**: Sample itineraries ranging from 2-8 nights
- **MCP Integration**: Full Model Context Protocol support for AI assistants

## Installation

1. Ensure you have Python 3.8+ installed

2. Install uv (fast Python package installer) from [here](https://docs.astral.sh/uv/getting-started/installation/):

3. Clone this repository and navigate to the project directory:

   ```bash
   git clone https://github.com/aryanranderiya/itinerary-mcp-server
   cd itinerary-mcp-server
   ```

4. Create a virtual environment and install dependencies:

   ```bash
   uv venv
   uv sync
   ```

5. Activate the virtual environment:

   **On Linux/macOS:**

   ```bash
   source .venv/bin/activate
   ```

   **On Windows (Command Prompt):**

   ```cmd
   .venv\Scripts\activate.bat
   ```

   **On Windows (PowerShell):**

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

## Running the Project

### Development Mode

Run the server in development mode with auto-reload:
Only run in development mode if you need to edit the code.

```bash
fastapi dev
```

### Production Mode

Run the server in production mode:

```bash
fastapi start
```

The API will be available at `http://localhost:8000` and the API documentation at `http://localhost:8000/docs`.

## Using the Model Context Protocol (MCP)

This project implements the [Model Context Protocol (MCP)](https://github.com/microsoft/model-context-protocol), which enables AI assistants to interact with your API directly. This means AI tools can understand your API's capabilities, data structures, and execute operations on your behalf.

### MCP Configuration

The project is already configured with the necessary MCP setup:

- **fastapi_mcp Library**: We use [fastapi_mcp](https://fastapi-mcp.tadata.com/) library to integrate MCP functionality with FastAPI
- **mcp.json**: The configuration is located in the `.vscode/mcp.json` file, which defines the MCP server settings:
  ```json
  {
    "servers": {
      "stay-often-mcp1": {
        "type": "sse",
        "url": "http://localhost:8000/mcp"
      }
    }
  }
  ```
  This configuration connects to the MCP endpoint at `http://localhost:8000/mcp` using Server-Sent Events (SSE).

No additional setup is required to use the MCP functionality - it's built into the server and ready to use.

### Supported MCP Clients

You can use any MCP-compatible client to interact with this API. MCP clients include:

- [GitHub Copilot](https://github.com/features/copilot)
- [Claude Desktop](https://claude.ai/download)
- And other MCP-compatible assistants

For more information about MCP, visit the [official MCP documentation](https://modelcontextprotocol.io/).

### Example: Using with GitHub Copilot

Here's how you can interact with this API using GitHub Copilot:

1. Start the server:

   ```bash
   fastapi dev
   ```

2. In your conversation with GitHub Copilot, you can request operations like:

   - **Get all itineraries**:

     ```
     Can you show me all the recommended itineraries for Phuket?
     ```

   - **Get a specific itinerary**:

     ```
     Show me the details for itinerary ID 3
     ```

   - **Create a new itinerary**:
     ```
     Create a new 5-night itinerary in Krabi with the following details: Name: "Krabi Adventure", day 1 at hotel 5 with activities 10 and 11, day 2 at hotel 5 with activity 12, etc.
     ```

GitHub Copilot will understand these requests and execute the appropriate API calls on your behalf through the MCP protocol.

## Screenshots
![Screenshot from 2025-04-30 02-25-34](https://github.com/user-attachments/assets/8eef9a6e-5b78-44e7-b134-c1600c20a4a0) 
![Screenshot from 2025-04-30 02-27-45](https://github.com/user-attachments/assets/5e876ba6-d73d-45cf-801b-28d6b36ba6ea)
<!--
![Screenshot from 2025-04-30 02-26-30](https://github.com/user-attachments/assets/c725cc9b-d6a5-4cb0-b153-c3aa15eee096)
![Screenshot from 2025-04-30 02-28-28](https://github.com/user-attachments/assets/6c7fdd95-f1b4-4a92-8e38-34a052a2bd0d)
![Screenshot from 2025-04-30 02-30-59](https://github.com/user-attachments/assets/7eaf3ba2-c8e7-4def-ba32-87c37d54210a)
-->
![Screenshot from 2025-04-30 02-49-00](https://github.com/user-attachments/assets/df06713d-c46a-4020-9b0c-72ae4a2d3516)
![Screenshot from 2025-04-30 02-34-12](https://github.com/user-attachments/assets/32768c07-fcfe-4941-aed8-16cef9b151cb)
![Screenshot from 2025-04-30 02-34-33](https://github.com/user-attachments/assets/ccc6d14a-9b37-41a1-9c26-23088b2f27e2)
![Screenshot from 2025-04-30 02-36-44](https://github.com/user-attachments/assets/c75344bb-a624-4c63-a214-efb89c502a11)


