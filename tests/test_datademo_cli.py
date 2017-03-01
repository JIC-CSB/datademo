"""Test the datademo CLI tool."""

import subprocess

from . import dataset_fixture  # NOQA


def test_version():
    cmd = ["datademo", "--version"]
    version = subprocess.check_output(cmd).decode("utf-8")
    assert version.startswith("datademo, version")


def test_dataset_identifiers(dataset_fixture):  # NOQA
    cmd = ["datademo", "dataset", "identifiers", dataset_fixture]
    identifiers = subprocess.check_output(cmd).decode("utf-8")
    assert len(identifiers.split()) == 2
