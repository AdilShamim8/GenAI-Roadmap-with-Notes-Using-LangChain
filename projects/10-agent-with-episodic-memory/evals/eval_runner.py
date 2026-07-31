"""Eval runner. Loads golden.jsonl, runs the agent, scores outputs, prints report."""
import json
import sys
from pathlib import Path


def load_golden(path: str = "evals/golden.jsonl") -> list[dict]:
    """Load the golden dataset."""
    cases = []
    for line in Path(path).read_text().splitlines():
        if line.strip():
            cases.append(json.loads(line))
    return cases


def run_agent(input_text: str) -> str:
    """TODO: replace with your actual agent call."""
    # from src import agent
    # return agent.run(input_text)
    return "REPLACE_WITH_AGENT_OUTPUT"


def score(output: str, expected: dict) -> bool:
    """Score an output against expected rubric."""
    out_lower = output.lower()
    must_mention = expected.get("must_mention", [])
    must_not_mention = expected.get("must_not_mention", [])
    return (
        all(kw.lower() in out_lower for kw in must_mention)
        and not any(kw.lower() in out_lower for kw in must_not_mention)
    )


def main():
    cases = load_golden()
    results = []
    for case in cases:
        output = run_agent(case["input"])
        passed = score(output, case["expected"])
        results.append({"id": case["id"], "passed": passed, "output": output})
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {case['id']}")

    passed = sum(r["passed"] for r in results)
    total = len(results)
    pass_rate = passed / total if total else 0
    print(f"\n{passed}/{total} passed ({pass_rate:.1%})")

    Path("evals/report.json").write_text(json.dumps(results, indent=2))

    if pass_rate < 0.85:
        print("FAIL: pass rate below threshold (0.85)")
        sys.exit(1)


if __name__ == "__main__":
    main()
