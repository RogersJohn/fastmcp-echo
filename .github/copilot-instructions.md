# FastMCP Echo Server - AI Coding Agent Instructions

## Project Overview
This is a **FastMCP server** implementing the Model Context Protocol (MCP) for AI assistant integration. It provides simple text manipulation tools (`echo` and `word_count`) that can be invoked by MCP clients like Claude Desktop or other AI assistants.

**Key Architecture**: Uses `fastmcp` library (v2.14.2+) which wraps Python functions as MCP tools and handles stdio transport for client communication.

## Critical FastMCP Pattern
When tools are defined using `@mcp.tool()` decorator in [server.py](server.py), FastMCP wraps them in `FunctionTool` objects. This is critical for testing:

```python
# In server.py - tools are wrapped by FastMCP
@mcp.tool(description="Echo text back with optional casing tweaks")
def echo(text: str, upper: bool = False) -> str:
    return text.upper() if upper else text

# In tests/test_server.py - unwrap to test the underlying function
from server import echo
echo = echo.fn  # Access underlying function via .fn attribute
```

**Always access `.fn` when testing FastMCP-decorated functions** (see [tests/test_server.py](tests/test_server.py#L5-L7)).

## Development Workflow

### Running the Server
```bash
python server.py  # Starts MCP server on stdio (for MCP clients)
```
The server uses stdio transport by default via `mcp.run()`, designed to be invoked by MCP clients, not run standalone.

### Testing
```bash
pytest                    # Run all tests
pytest tests/test_server.py  # Run specific test file
pytest -k "test_echo"    # Run tests matching pattern
```

**Test organization**: Tests are grouped by function into classes (`TestEcho`, `TestWordCount`) with three sections:
- Positive Tests: Normal functionality
- Edge Case Tests: Boundary conditions (empty strings, unicode, whitespace)
- Negative Tests: Invalid inputs that should raise exceptions

### Environment
- Python 3.11+ required (see [pyproject.toml](pyproject.toml))
- Uses `uv` for dependency management (note `uv.lock` file)
- Virtual environment in `.venv/`

## Code Conventions

### Tool Definitions
- Use `@mcp.tool()` decorator with descriptive `description` parameter
- Tool functions must have type hints for all parameters and return values
- Keep tool functions simple - single responsibility
- Default parameters should be documented in function signature

### Testing Standards
- Comprehensive test coverage: positive cases, edge cases, and negative cases
- Use descriptive test names: `test_<function>_<scenario>()`
- Test docstrings explain what is being tested
- Negative tests use `pytest.raises()` to verify proper error handling

### Error Handling
Functions raise `TypeError` when passed non-string types (see negative tests). This is implemented via explicit type validation that checks `isinstance(text, str)` and provides clear error messages indicating the expected and received types.

## Adding New Tools
1. Define function in [server.py](server.py) with `@mcp.tool()` decorator
2. Add type hints and description
3. Create corresponding test class in [tests/test_server.py](tests/test_server.py)
4. Remember to unwrap with `.fn` in tests before testing the function
5. Write positive, edge case, and negative tests
