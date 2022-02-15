import os
import shutil

from log import log, BOLD, END, GREEN

DIST_DIR = "./dist"


def smart_make_dist_dir():
    """Create `dist` directory if it doesn't exist already"""

    log(f"Creating empty {BOLD}dist{END}{GREEN} directory")

    if os.path.isdir(DIST_DIR):
        try:
            shutil.rmtree(DIST_DIR)
        except OSError as err:
            print("Error: %s : %s" % (DIST_DIR, err.strerror))
    os.mkdir(DIST_DIR)


def make_osk():
    """zip the `dist` directory and save it to `POMP.osk`"""

    log(f"Creating {BOLD}POMP.osk")

    shutil.make_archive("POMP", "zip", DIST_DIR)

    if os.path.isfile("POMP.zip"):
        os.rename("POMP.zip", "POMP.osk")
    else:
        print_error("cannot find zip file to convert to osk file :(")
