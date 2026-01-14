from fastmcp import FastMCP

mcp = FastMCP("echo-server", version="0.1.0")

@mcp.tool(description="Echo text back with optional casing tweaks")
def echo(text: str, upper: bool = False) -> str:
    """Return the submitted text."""
    if not isinstance(text, str):
        raise TypeError(f"'text' must be a string, got {type(text).__name__}")
    return text.upper() if upper else text

@mcp.tool
def word_count(text: str) -> int:
    """Count characters separated by whitespace."""
    if not isinstance(text, str):
        raise TypeError(f"'text' must be a string, got {type(text).__name__}")
    return len(text.split())

if __name__ == "__main__":
    mcp.run()  # defaults to stdio transport for local clients
