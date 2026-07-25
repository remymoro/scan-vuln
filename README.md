# scan-vuln

`scan-vuln` is an extensible web security assessment tool for authorized
targets. It runs security checks, identifies potential vulnerabilities and
misconfigurations, and produces an actionable report.

## Scope

The project is designed around independent security-check modules. Planned
checks include:

- TLS configuration;
- HTTP security headers;
- WAF presence and configuration signals;
- dependency and known-vulnerability analysis;
- additional active, non-destructive checks.

The first implementation will focus on one small, testable module before the
scanner expands to the other checks.

## Authorized Use

Use this tool only against systems for which you have explicit authorization.
The default behavior must remain rate-limited and non-destructive. Future active
checks must preserve these constraints.

## Reports

Every check will return findings with a common structure:

- check identifier and module;
- severity and status;
- title and observed evidence;
- potential impact;
- remediation recommendation.

The scanner will first provide machine-readable JSON reports. Other report
formats can be added later without changing the check modules.

## Development

The project uses `uv` for dependency and environment management.

```bash
uv sync
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

## Project Status

The development environment is configured with Python 3.12, Ruff, and Pytest.
Security-check modules and the scan-report workflow are not implemented yet.
