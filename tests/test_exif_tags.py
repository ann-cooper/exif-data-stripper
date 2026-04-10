import pytest
from PIL.ExifTags import TAGS


@pytest.fixture(scope="function")
def common_tags():
    return {
        34853: "GPSInfo",
        296: "ResolutionUnit",
        34665: "ExifOffset",
        271: "Make",
        272: "Model",
        305: "Software",
        274: "Orientation",
        306: "DateTime",
        531: "YCbCrPositioning",
        282: "XResolution",
        283: "YResolution",
        316: "HostComputer",
    }


def test_artist_at_315():

    assert TAGS.get(315) == "Artist"


def test_copyright_at_33432():

    assert TAGS.get(33432) == "Copyright"


def test_orientation_at_274():

    assert TAGS.get(274) == "Orientation"


def test_common_tags_to_keys(common_tags):
    """Look up each tag in the common_tags keys list and make sure
    that the Pillow TAGS dict still returns the expected text value.
    To check whether anything changed if Pillow req is updated.
    """

    assert {k: TAGS.get(k) for k in list(common_tags.keys())} == common_tags
