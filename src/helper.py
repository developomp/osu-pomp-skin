"""A collection of helper functions"""

import os
import shutil
from glob import glob

from log import info, BOLD, END, GREEN

DIST_DIR = "./dist"


def smart_make_dist_dir():
    """Create `dist` directory if it doesn't exist already"""

    info(f"Creating empty {BOLD}dist{END}{GREEN} directory")

    if os.path.isdir(DIST_DIR):
        try:
            shutil.rmtree(DIST_DIR)
        except OSError as err:
            print("Error: %s : %s" % (DIST_DIR, err.strerror))
    os.mkdir(DIST_DIR)


def make_osk():
    """zip the `dist` directory and save it to `POMP.osk`"""

    info(f"Creating {BOLD}POMP.osk")

    shutil.make_archive("POMP", "zip", DIST_DIR)

    if os.path.isfile("POMP.zip"):
        os.rename("POMP.zip", "POMP.osk")
    else:
        print_error("cannot find zip file to convert to osk file :(")


def copy_all(glob_pattern: str):
    """Copy all files in a path"""

    # find all files
    for file_path in glob(glob_pattern):
        # ignore files
        if "/__init__.py" in file_path or "/__pycache__" in file_path:
            continue

        # copy file
        file_name = file_path.split("/")[-1]
        shutil.copyfile(file_path, f"dist/{file_name}")
