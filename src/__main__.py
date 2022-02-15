#!/usr/bin/env python

from os import chdir, getcwd
from os.path import dirname, realpath, isdir, join, realpath

from log import BOLD, END, INVERSE, err
import util


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
    util.smart_make_dist_dir()


def main():
    welcome()
    initialize()

    # create POMP.osk
    util.make_osk()


main()
