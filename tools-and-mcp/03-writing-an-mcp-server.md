# Writing an MCP Server

> **Level:** INT · **Last verified:** 2026-07-30

## Why this matters

Off-the-shelf MCP servers cover common cases (filesystem, Postgres, GitHub). But the moment you have an internal API, a custom database, or a domain-specific tool, you need to write your own. It's a 50-line exercise in Python.

## Core concepts

### The MCP Python SDK

```bash
pip install mcp
```

The SDK exposes a `Server` class. You register handlers for `tools/list`, `tools/call`, `resources/list`, `resources/read`.

### The lifecycle

1. Server starts, registers handlers.
2. Client connects, requests capability negotiation.
3. Client calls `tools/list` → server returns tool schemas.
4. Client (on behalf of LLM) calls `tools/call` with a tool name + args.
5. Server executes, returns result.
6. Repeat.

## Code: a Postgres-querying MCP server

```python
# server.py
from mcp.server import Server
from mcp.types import Tool, TextContent
import psycopg2, json

server = Server("postgres-readonly")
conn = psycopg2.connect("dbname=sales user=readonly host=localhost")

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [Tool(
        name="query_sales",
        description="Run a read-only SQL query against the sales database. SELECT only.",
        inputSchema={
            "type": "object",
            "properties": {"sql": {"type": "string", "description": "SELECT query"}},
            "required": ["sql"],
        },
    )]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name != "query_sales":
        raise ValueError(f"Unknown tool: {name}")
    sql = arguments["sql"].strip()
    if not sql.lower().startswith("select"):
        return [TextContent(type="text", text="Error: only SELECT queries allowed.")]
    with conn.cursor() as cur:
        cur.execute(sql)
        cols = [d[0] for d in cur.description]
        rows = cur.fetchall()
    return [TextContent(type="text", text=json.dumps({"columns": cols, "rows": rows}, default=str))]

if __name__ == "__main__":
    import asyncio
    from mcp.server.stdio import stdio_server
    async def main():
        async with stdio_server() as (read, write):
            await server.run(read, write, server.create_initialization_options())
    asyncio.run(main())
```

Run with an MCP-aware client (Claude Desktop, Cursor, your own agent).

## Production concerns

- **Latency:** Each tool call is a request/response. Use connection pooling for DB-backed servers.
- **Cost:** Self-hosted; the cost is your infra.
- **Failure modes:** Unhandled exceptions in a tool handler crash the server. Wrap everything in try/except.
- **Security:** Enforce least privilege at the server level. Don't trust the LLM to police itself.

## Anti-patterns

- ❌ **Exposing mutating SQL (INSERT/UPDATE/DELETE).** Use read-only DB users.
- ❌ **Returning huge result sets.** Paginate or summarize.
- ❌ **Hardcoding credentials.** Use env vars.

## References

- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) — verified 2026-07-30
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) — verified 2026-07-30
