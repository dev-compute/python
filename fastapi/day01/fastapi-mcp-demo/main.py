from fastapi import FastAPI
from fastmcp import FastMCP


# 1. Create the MCP server
mcp = FastMCP("Calculator MCP Server")


# 2. Register a tool with the MCP server
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


# 3. Create an ASGI application from FastMCP
mcp_app = mcp.http_app(path="/")


# 4. Create the main FastAPI application
app = FastAPI(lifespan=mcp_app.lifespan)


# 5. Define a normal FastAPI endpoint
@app.get("/health")
def health():
    return {"status": "healthy"}


# 6. Mount the MCP application inside FastAPI
app.mount("/mcp", mcp_app)
