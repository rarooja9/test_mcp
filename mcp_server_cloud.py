"""
MCP Server with say_hello tool - FastMCP Cloud Deployment
"""
from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Hello Server")

@mcp.tool()
def say_hello(name: str) -> str:
    """
    Generate a personalized greeting for the given name.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        A personalized greeting message
    """
    return f"Hello, {name}! Welcome to the FastMCP Cloud server!"

# For local testing
if __name__ == "__main__":
    mcp.run()
