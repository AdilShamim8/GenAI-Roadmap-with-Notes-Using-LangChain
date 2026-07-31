# Deployment — Eval-Driven Prompt Refinement Harness

## Local

```bash
make install
make run
```

## Docker

```bash
docker build -t 07-eval-driven-prompt-refinement .
docker run -p 8000:8000 --env-file .env 07-eval-driven-prompt-refinement
```

## Production (illustrative)

Recommended deployment pattern for this project:

1. **Containerize** with the included `Dockerfile` (TODO: write it).
2. **Deploy** to Fly.io / Render / Railway for a free-tier demo.
3. **Observe** with OpenTelemetry → Arize Phoenix.
4. **Alert** on cost > 2× daily baseline.
5. **Kill switch** via feature flag (Statsig / LaunchDarkly).

## Cost budget

- Per-request cost target: $0.05 max
- Daily budget: $10
- Alert at 50%, 80%, 100% of budget

## Postmortem template

When this project breaks in production (it will), write a postmortem:

```markdown
# Postmortem — YYYY-MM-DD

## Summary
[One sentence.]

## Timeline
- HH:MM Detection
- HH:MM Mitigation
- HH:MM Resolution

## Root cause
[Technical.]

## Contributing factors
[Process / cultural.]

## Action items
- [ ] ...
- [ ] ...

## Lessons
[What we learned.]
```
