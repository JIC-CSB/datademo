"""Test the datademo CLI tool."""

import subprocess


def test_version():
    cmd = ["datademo", "--version"]
    version = subprocess.check_output(cmd).decode("utf-8")
    assert version.startswith("datademo, version")
