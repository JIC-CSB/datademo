"""Test fixtures."""

import os
import shutil
import tempfile

import pytest
import dtool

_HERE = os.path.dirname(__file__)


@pytest.fixture
def chdir_fixture(request):
    d = tempfile.mkdtemp()
    curdir = os.getcwd()
    os.chdir(d)

    @request.addfinalizer
    def teardown():
        os.chdir(curdir)
        shutil.rmtree(d)


@pytest.fixture
def tmp_dir_fixture(request):
    d = tempfile.mkdtemp()

    @request.addfinalizer
    def teardown():
        shutil.rmtree(d)
    return d


@pytest.fixture
def local_tmp_dir_fixture(request):
    d = tempfile.mkdtemp(dir=_HERE)

    @request.addfinalizer
    def teardown():
        shutil.rmtree(d)
    return d


@pytest.fixture
def dataset_fixture(request):
    d = tempfile.mkdtemp()

    dataset = dtool.DataSet("test", "data")
    dataset.persist_to_path(d)

    for s in ["hello", "world"]:
        fname = s + ".txt"
        fpath = os.path.join(d, "data", fname)
        with open(fpath, "w") as fh:
            fh.write(s)

    dataset.update_manifest()

    @request.addfinalizer
    def teardown():
        shutil.rmtree(d)
    return d


@pytest.fixture
def project_fixture(request):
    project_path = tempfile.mkdtemp()

    project_name = "crop_yield"
    project = dtool.Project(project_name)
    project.persist_to_path(project_path)

    for ds_name in ["rice", "wheat", "barley"]:

        ds_path = os.path.join(project_path, ds_name)
        os.mkdir(ds_path)

        dataset = dtool.DataSet(ds_name, "data")
        dataset.persist_to_path(ds_path)

        for s in ["sow", "grow", "harvest"]:
            fname = s + ".txt"
            fpath = os.path.join(ds_path, "data", fname)
            with open(fpath, "w") as fh:
                fh.write("{} {}\n".format(s, ds_name))

        dataset.update_manifest()

    @request.addfinalizer
    def teardown():
        shutil.rmtree(project_path)
    return project_path
