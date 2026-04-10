import os
from pathlib import Path

import click
from PIL import Image

from exif_util.helpers import set_paths
from exif_util.process_exif_data import ExifProcessor


@click.command()
@click.option(
    "--source_directory",
    default="strip",
    prompt="(Optional) Name of the folder containing images files to process through the exif data stripper. Defaults to ~Desktop/strip.",
    help="Assumes folder is located under ~/Desktop. Example ~/Desktop/images_to_strip.",
    required=False,
)
@click.option(
    "--target_directory",
    default="ready",
    prompt="(Optional) Where to store the stripped and updated image files. Defaults to ~Desktop/ready.",
    help="(Optional) Where to store the stripped and updated image files. This should be an existing folder under ~Desktop/. Defaults to ~Desktop/ready.",
    required=False,
)
@click.option(
    "--artist",
    prompt="(Required) Photographer's name",
    required=True,
    help="Photograpber's name.",
)
def app(
    artist: str,
    source_directory: str = None,
    target_directory: str = None,
):

    if not source_directory:
        source_directory = "strip"
    if not target_directory:
        target_directory = "ready"

    DESKTOP = os.path.expanduser("~/Desktop")
    target = Path(DESKTOP + "/" + target_directory)

    paths = set_paths(desktop=DESKTOP, source_dir=source_directory)

    for path in paths:
        with Image.open(path) as img:
            e_processor = ExifProcessor(
                img_path=path, img=img, target_folder=target, artist=artist
            )
            e_processor.run_exif_processor()


if __name__ == "__main__":
    app()
