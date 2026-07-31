# Anthropic Claude Agent SDK

> **Level:** INT · **Last verified:** 2026-07-30

## Why this matters

Anthropic's Claude Agent SDK (the evolution of the Claude Code internals) is purpose-built for long-horizon, file-operating agents. If your agent needs to read/write files, run commands, and persist state across hours of work, this is the strongest choice in 2026.

## Core concepts

### The primitives

- **Agent** — system prompt + model + tools + (optional) file sandbox.
- **Tool** — built-in (Bash, file edit, search) or custom.
- **Sandbox** — a directory the agent can read/write; everything else is read-only.
- **Session** — durable agent state, resumable.

### Built-in tools

The SDK ships with high-quality implementations of:
- `bash` — run shell commands in the sandbox.
- `file_edit` — atomic file edits with diff.
- `file_read` — read files with line ranges.
- `grep` — search files.
- `web_search` / `web_fetch` — retrieve from the web.

These are battle-tested from Claude Code. Don't reimplement.

## Code: minimal agent

```python
from claude_agent_sdk import Agent, ClaudeAgentOptions

agent = Agent(ClaudeAgentOptions(
    model="claude-sonnet-4-5",
    system_prompt="You are a coding assistant. Edit files in the current directory.",
    working_directory="/tmp/agent-workspace",
    allowed_tools=["bash", "file_edit", "file_read", "grep"],
))

result = await agent.run("Add a docstring to every function in utils.py.")
print(result.final_message)
```

## Code: custom tool

```python
from claude_agent_sdk import tool

@tool
def query_db(sql: str) -> str:
    '''Run a read-only SQL query.'''
    # ... execute and return as string
    return json.dumps(rows)
```

## Production concerns

- **Latency:** Long-horizon agents can run for minutes to hours. Stream progress.
- **Cost:** Token usage scales with file sizes the agent reads. Limit context.
- **Failure modes:** Agents can delete files in their sandbox. Use version control.
- **Security:** Sandbox boundaries are critical. Never run with `working_directory=/`.

## Anti-patterns

- ❌ **Running the agent with no sandbox.** Catastrophic.
- ❌ **Giving the agent write access to your repo without git.** You can't undo.
- ❌ **Ignoring the agent's bash output.** Read every command.

## References

- [Claude Agent SDK (Python)](https://github.com/anthropics/claude-agent-sdk-python) — verified 2026-07-30
- [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code) — verified 2026-07-30
