# flaky-test-quarantine

A minimal, runnable example for the InfraCraft Labs guide
[Flaky tests in CI: quarantine them, don't retry until green](https://infracraftlabs.com/insights/quarantine-flaky-tests/).

One test file has two stable tests and one deterministic stand-in for a flaky test: it fails on the first
attempt in a run and passes on the next. The workflow runs it three ways:

| Job | Command | Purpose |
| --- | --- | --- |
| `tests` | `pytest -m "not quarantine"` | The only required check. Stable tests block merges. |
| `quarantine` | `pytest -m quarantine`, `continue-on-error: true` | Runs and reports the flaky test without blocking. Accepts exit 5 (nothing quarantined) and fails if more than 10 tests are quarantined. |
| `retries-demo` | `pytest --reruns 2` | For comparison: the retry turns the failing test green. |

## Run locally

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/pytest --reruns 2          # 3 passed, 1 rerun, exit 0
.venv/bin/pytest -m "not quarantine" # 2 passed, exit 0
.venv/bin/pytest -m quarantine       # 1 failed, exit 1
```

Delete `/tmp/flaky-state` (or set `FLAKY_STATE` to a new path) between runs, so the flaky test starts again.

## License

MIT
