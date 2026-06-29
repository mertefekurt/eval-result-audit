# eval-result-audit

`eval-result-audit` is a small local CLI that audit LLM evaluation result exports for gaps, weak judges, and missing rationales.

## Why it is useful

Eval results become hard to trust when cases lack rationales or judge metadata. This CLI catches gaps in exported eval runs.

## Key features

- reads text, JSON, JSONL, or CSV inputs
- returns Markdown or JSON reports
- supports severity-based CI exit codes
- keeps all checks deterministic and offline
- includes focused rules for this project:
- `unknown-judge`: judge identity is missing
- `missing-rationale`: judge rationale is missing
- `skipped-case`: eval case was skipped

## Installation

```bash
python -m pip install -e ".[dev]"
```

## Usage

```bash
eval-result-audit examples/sample.txt
eval-result-audit examples/sample.txt --json
eval-result-audit path/to/input.txt --fail-on medium --out report.md
python -m eval_result_audit --help
```

Example input:

```text
case 42 score pass judge: unknown rationale: missing skipped false
```

## CLI options

```text
eval-result-audit INPUT [--format auto|text|jsonl|csv|json] [--json]
             [--fail-on low|medium|high] [--out PATH]
```

`INPUT` is any eval result JSONL, CSV, or notes. The tool exits with code `2` when findings meet the selected
threshold, which makes it easy to use in GitHub Actions or release checks.

## Workflow

```mermaid
flowchart LR
    A[input file] --> B[format reader]
    B --> C[project-specific rules]
    C --> D[risk score]
    D --> E[Markdown or JSON report]
```

## Tests

```bash
ruff check .
pytest
python -m eval_result_audit --help
```

## License

MIT
