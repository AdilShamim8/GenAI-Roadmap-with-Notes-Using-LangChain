.PHONY: install run test eval lint clean

install:
	pip install -e ".[dev]"

run:
	python -m src

test:
	pytest tests/ -v

eval:
	python evals/eval_runner.py

lint:
	ruff check . && ruff format --check .

clean:
	rm -rf .pytest_cache __pycache__ .ruff_cache
