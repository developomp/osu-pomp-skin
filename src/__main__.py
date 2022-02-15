#!/usr/bin/env python

from os import chdir, getcwd
from os.path import dirname, realpath, isdir, join, realpath
from importlib.util import spec_from_file_location, module_from_spec
from glob import glob

from log import BOLD, END, INVERSE, GREEN, err, info
from helper import smart_make_dist_dir, make_osk
import sys


def welcome():
    print(
        f"{BOLD}────────────────────{END}{INVERSE}  POMP's osu! skin  {END}{BOLD}────────────────────{END}"
    )


def initialize():
    # move to project root
    chdir(realpath(join(dirname(realpath(__file__)), "..")))

    print(f"working directory: {BOLD}{getcwd()}{END}")
    print()

    # crete dist directory
    smart_make_dist_dir()


def run_procedures():
    """Import and execute all `setup.py` files in the `procedures` directory."""

    for setup_script_path in glob("src/procedures/*/setup.py"):
        module_name = setup_script_path.split("/")[-2]

        info(f"Parsing {BOLD}{module_name}{END}{GREEN}")

        spec = spec_from_file_location(module_name, setup_script_path)
        module = module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)


def main():
    welcome()
    initialize()

    run_procedures()

    # create POMP.osk
    make_osk()


main()
