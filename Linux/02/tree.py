#!/usr/bin/env python3
import os


def walking(path, in_dir=False):
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and not entry.is_symlink():
                if entry.is_dir():
                    print(entry.name + "/")
                    walking(entry.path, in_dir=True)
                else:
                    if in_dir:
                        print("    " + entry.name)
                    else:
                        print(entry.name)


if __name__ == '__main__':
    walking(input())
