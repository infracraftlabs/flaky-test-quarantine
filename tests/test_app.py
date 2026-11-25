import os
import pathlib

import pytest

STATE = pathlib.Path(os.environ.get("FLAKY_STATE", "/tmp/flaky-state"))


def test_add():
    assert 1 + 1 == 2


def test_parse():
    assert int("42") == 42


@pytest.mark.quarantine  # stand-in for a tracked issue: owner and target date
def test_upload_retries_on_timeout():
    # Deterministic stand-in for a flaky test: fails on the first attempt in a run, passes on the next.
    n = int(STATE.read_text()) if STATE.exists() else 0
    STATE.write_text(str(n + 1))
    assert n % 2 == 1, "timeout talking to the fake upload service"
