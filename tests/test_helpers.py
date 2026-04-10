import pytest

from exif_util.helpers import set_paths


def test_helpers():
    paths = set_paths(desktop="tests/tmpdata", source_dir="strip")

    assert len(paths) == 3
