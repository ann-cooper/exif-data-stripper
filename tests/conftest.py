from pathlib import Path

import piexif
import pytest
from piexif import GPSIFD, ImageIFD
from PIL import ExifTags, Image

from exif_util.helpers import set_paths
from exif_util.process_exif_data import ExifProcessor


def desktop_path():
    """Create temporary directory structure to save image file test doubles."""
    Path("tests/tmpdata").mkdir()
    Path("tests/tmpdata/strip").mkdir()
    Path("tests/tmpdata/ready").mkdir()


@pytest.fixture(scope="session", autouse=True)
def images():
    desktop_path()

    basic_info = {ImageIFD.Make: b"SomeMake", ImageIFD.Orientation: 1}
    gps = {
        GPSIFD.GPSLatitudeRef: b"N",
        GPSIFD.GPSLatitude: [(40, 1), (730, 100)],
        GPSIFD.GPSLongitudeRef: b"W",
        GPSIFD.GPSLongitude: [(73, 1), (935, 1)],
        GPSIFD.GPSAltitudeRef: 0,
        GPSIFD.GPSAltitude: (1000, 1),
        GPSIFD.GPSDateStamp: b"2025:12:10",
    }
    exif_dict = {"0th": basic_info, "GPS": gps}
    for n in range(4):
        test_img = Image.new(mode="1", size=(2, 3))
        test_img_path = Path("tests/tmpdata/strip" + "/" + f"test_image_{n}.jpg")
        exif_bytes = piexif.dump(exif_dict)
        test_img.save(test_img_path, exif=exif_bytes)


@pytest.fixture(scope="function")
def fake_paths():
    return set_paths(desktop="tests/tmpdata", source_dir="strip")


@pytest.fixture(scope="function")
def instantiate_processor(fake_paths):
    test_path = fake_paths[0]
    with Image.open(test_path) as test_img:
        processor = ExifProcessor(
            img_path=test_path,
            img=test_img,
            target_folder=Path("tests/tmpdata/ready"),
            artist="Test Artist",
        )
    return processor


@pytest.fixture(scope="session", autouse=True)
def cleanup():
    """Remove test files and directories after test session."""

    yield
    strip_path = Path("tests/tmpdata/strip")
    ready_path = Path("tests/tmpdata/ready")

    for file in strip_path.iterdir():
        file.unlink()
    for file in ready_path.iterdir():
        file.unlink()

    strip_path.rmdir()
    ready_path.rmdir()
    Path("tests/tmpdata").rmdir()

