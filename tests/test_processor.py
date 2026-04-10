from pathlib import Path

from exif_util.process_exif_data import ExifProcessor as EP


def test_run_exif_processor(instantiate_processor):

    instantiate_processor.run_exif_processor()

    target = Path("tests/tmpdata/ready")
    assert (target / "test_image_3.jpg").is_file()


def test_instantiate(instantiate_processor):
    """Spot check expected values."""

    assert instantiate_processor.artist == "Test Artist"
    assert instantiate_processor.target_folder == Path("tests/tmpdata/ready")
