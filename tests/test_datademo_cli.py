"""Test the datademo CLI tool."""

import os
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


def test_dataset_paths(dataset_fixture):  # NOQA
    cmd = ["datademo", "dataset", "paths", dataset_fixture]
    output_string = subprocess.check_output(cmd).decode("utf-8")
    paths = output_string.split()
    assert len(paths) == 2
    for path in paths:
        assert os.path.isfile(path)


def test_dataset_manifest(dataset_fixture):  # NOQA
    import json
    import dtool
    cmd = ["datademo", "dataset", "manifest", dataset_fixture]
    manifest_str = subprocess.check_output(cmd).decode("utf-8")
    manifest = json.loads(manifest_str)
    dataset = dtool.DataSet.from_path(dataset_fixture)
    assert manifest == dataset.manifest


def test_dataset_summary(dataset_fixture):  # NOQA
    import json
    import getpass
    cmd = ["datademo", "dataset", "summary", dataset_fixture]
    summary_str = subprocess.check_output(cmd).decode("utf-8")
    summary = json.loads(summary_str)
    expected = {
        "Name": "test",
        "Creator": getpass.getuser(),
        "Number of files": 2,
        "Total size": 10,
    }
    assert summary == expected
