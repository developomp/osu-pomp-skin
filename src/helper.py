"""A collection of helper functions"""

import os
import shutil
from glob import glob

from log import err

DIST_DIR = "./dist"


def smart_make_dist_dir():
    """Create `dist` directory if it doesn't exist already"""

    if os.path.isdir(DIST_DIR):
        try:
            shutil.rmtree(DIST_DIR)
        except OSError as err:
            print("Error: %s : %s" % (DIST_DIR, err.strerror))
    os.mkdir(DIST_DIR)


def make_osk():
    """zip the `dist` directory and save it to `POMP.osk`"""

    shutil.make_archive("POMP", "zip", DIST_DIR)

    if os.path.isfile("POMP.zip"):
        os.rename("POMP.zip", "POMP.osk")
    else:
        err("cannot find zip file to convert to osk file :(")


def copy_all(
    glob_pattern: str, add_postfix=False, exclude=["/__init__.py", "/__pycache__"]
):
    """Copy all files in a path"""

    # find all files
    for file_path in glob(glob_pattern):
        # ignore files
        if any(exclude_condition in file_path for exclude_condition in exclude):
            continue

        # copy file
        file_name = file_path.split("/")[-1]

        if add_postfix:
            file_name = file_name.removesuffix(".png")
            shutil.copyfile(file_path, f"dist/{file_name}@2x.png")
            continue

        shutil.copyfile(file_path, f"dist/{file_name}")
