from datetime import datetime as dt
from pathlib import Path

from PIL import Image
from PIL.ExifTags import TAGS

from exif_util import logger

logger = logger.get_logger(__name__)


class ExifProcessor:
    """Strips exif data from individual image files and adds copyright and artist info.

    Attributes
    ----------
    img_path: Path
        The location of the image being processed.
    img: Image
        The image file itself.
    target_folder: Path
        Where the processed image will be stored.
    artists: str
        The photographer's name.

    Methods
    -------
    strip_exif_data
        Strip all exif data but orientation, copyright, and artist.
    update_exif_data
        Update (overwrite) artist and copyright data.
    check_exif_data
        Returns a dict of {tag: value} of exif_data.
    move_image_file
        Move processed image to the target_folder.
    run_exif_processor
        Run all processing steps.

    """

    def __init__(
        self,
        img_path: Path,
        img,
        target_folder: Path,
        artist: str,
    ):
        self.img_path = img_path
        self.img = img.copy()
        self.target_folder = target_folder
        self.artist = artist

        self.exif_data = img.getexif()
        self.skip_tags = ["Artist", "Copyright", "Orientation"]

    def strip_exif_data(self):
        """Strip all exif data but orientation, copyright, and artist."""
        logger.info(f"Original exif data: {self.check_exif_data()}")
        logger.info(f"Stripping exif data on {self.img_path}")

        for k, v in self.exif_data.items():
            str_k = TAGS.get(k)
            if str_k not in self.skip_tags:
                del self.exif_data[k]

        return self

    def update_exif_data(self):
        """Update artist and copyright data.
        Note:
            Assumes that this information is not already present in the exif data.
            Overwrites values in "Artist" and "Copyright" tags.
        """
        year = dt.now().year
        copyright_info = f"Copyright {year} {self.artist}. All rights reserved."

        self.exif_data[315] = self.artist
        self.exif_data[33432] = copyright_info
        self.img.save(self.img_path, exif=self.exif_data)
        logger.info(f"Updated exif data: {self.check_exif_data()}")

        return self

    def check_exif_data(self):
        """Returns a dict of tag: value of exif_data."""

        return {TAGS.get(k): v for k, v in self.exif_data.items()}

    def move_image_file(self):
        """Move processed image to the target_folder."""
        self.target_folder.mkdir(exist_ok=True)
        target_path = Path(self.target_folder.as_posix() + "/" + self.img_path.name)

        logger.info(f"Moving {self.img_path} to {target_path}")
        self.img_path.rename(target_path)

        return self

    def run_exif_processor(self):
        """Run processing steps."""
        for step in [self.strip_exif_data, self.update_exif_data, self.move_image_file]:
            step()
