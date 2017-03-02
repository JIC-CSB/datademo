"""Test the datademo project CLI tool."""

import subprocess

from . import project_fixture  # NOQA


def test_dataset_summary(project_fixture):  # NOQA
    import json
    cmd = ["datademo", "project", "summary", project_fixture]
    summary_str = subprocess.check_output(cmd).decode("utf-8")
    summary = json.loads(summary_str)
    expected = {
        "Name": "crop_yield",
        "Number of datasets": 3,
        "Number of files": 9,
        "Total size": 105,
    }
    assert summary == expected
