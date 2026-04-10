import re
from pathlib import Path

import setuptools


def get_version():
    version_file = Path("src") / "__init__.py"
    with open(version_file) as vf:
        pattern = re.compile(r"((\d\.){2,}(\d))")
        version = vf.read()
        version = version.split("=")[1].strip()
        version = re.search(pattern, version).group(1)
    return version


def get_requirements():
    with open("requirements.txt", encoding="utf-8") as rf:
        reqs = rf.read()
        pattern = re.compile(r"^\w.*?")
        lines = reqs.split("\n")
        out_reqs = [line.split("==")[0] for line in lines if re.search(pattern, line)]

    return out_reqs


setuptools.setup(
    version=get_version(),
    description="A command-line exif stripper and copyright tool for photos.",
    install_requires=get_requirements(),
)
