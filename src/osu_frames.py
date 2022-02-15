#!/usr/bin/env python3

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from glob import glob
from time import sleep
from os import rename
from os.path import basename, join
from shutil import copyfile
from re import search


def increment_files(path, pattern, dry_run):
    deliminator = "-"
    files = sorted(glob(join(path, pattern)))
    print("Changing", len(files), "file names")

    for index, file in enumerate(files):
        file_name = basename(file)

        file_name_parts = file_name.split(deliminator)

        prefix = file_name_parts[0]
        postfix = file_name_parts[1]
        number_regex = search(r"\d+", postfix)
        number_span = number_regex.span()

        new_file_name = join(
            path, f"{prefix}{deliminator}{str(index)}{postfix[number_span[1]:]}"
        )

        if dry_run:
            print(f"{file} -> {new_file_name}")
        else:
            rename(file, new_file_name)
            sleep(0.1)


def make_100k_from_100(path, dry_run):
    files = sorted(glob(join(path, "hit100*")))
    print("Changing", len(files), "file names")

    for file in files:
        file_name = basename(file)

        new_file_name = join(path, f"hit100k{file_name[6:]}")

        if dry_run:
            print(f"{file} -> {new_file_name}")
        else:
            copyfile(file, new_file_name)
            sleep(0.1)


def parseargs():
    parser = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description="Increment file prefixes starting at a specific index.",
    )

    parser.add_argument(
        "path",
        help="where the files are located",
    )

    parser.add_argument(
        "-p",
        "--pattern",
        help="glob pattern of files that will be affected",
    )

    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="print the results instead of renaming the files",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parseargs()

    make_100k_from_100(args.path, args.dry_run)
    # increment_files(args.path, args.pattern, args.dry_run)
