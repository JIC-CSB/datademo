"""Test the datademo package."""


def test_version_is_string():
    import datademo
    assert isinstance(datademo.__version__, str)
