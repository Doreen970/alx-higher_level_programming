#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    total_args = sum(int(arg) for arg in agrv)
    print(total_args)
