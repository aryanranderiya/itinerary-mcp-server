import sys
import os

# Add the project root to the path to make app modules importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Now we can import from the app package
from app.mcp import tools
from app.mcp import mcp

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="stdio")
