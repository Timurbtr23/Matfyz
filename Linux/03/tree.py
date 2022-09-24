#!/usr/bin/env python3

import os
import sys


def look_for_d():
    if "-d" in sys.argv:
        return True
    else:
        return False


def which_directory():
    for arg in sys.argv:
        if arg != "-d" and arg != sys.argv[0]:
            return arg
    else:
        return os.path.dirname(__file__)


def sort_dir(given_path):
    with os.scandir(given_path) as it:
        direntries = list(it)

    direntries.sort(key=lambda x: x.name)
    return direntries


def print_tree(given_path, deep=0, d_factor=False):
    direntries = sort_dir(given_path)
    space_format = "    " * deep

    for sth in direntries:
        if not sth.name.startswith('.') and not sth.is_symlink():
            if sth.is_dir():
                print(space_format + sth.name + "/")
                print_tree(sth.path, deep + 1, d_factor)
            elif not d_factor:
                print(space_format + sth.name)


if __name__ == '__main__':
    dirs = look_for_d()
    path = which_directory()
    print_tree(path, d_factor=dirs)
