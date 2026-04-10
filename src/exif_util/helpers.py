from pathlib import Path

from exif_util import logger

logger = logger.get_logger(__name__)


def set_paths(desktop: str, source_dir: str = None) -> list:
    """Prepare list of image paths to strip. If no arguments passed,
    will prepare paths for all images in the ~/Desktop/strip folder.

    Args:
        desktop (list, optional): .
        source_dir (str, optional): All images in this directory should be processed. Defaults to "strip".

    Returns:
        list: A list of posix paths for the images to be stripped.
    """

    paths = [
        img
        for img in Path(desktop + "/" + source_dir).iterdir()
        if img.name != ".DS_Store"
    ]

    logger.info(f"Processing paths: {paths}")

    return paths
