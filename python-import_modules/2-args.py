#!/usr/bin/python3
import sys
nr_arg = len(sys.argv) - 1
for index, argument in enumerate(sys.argv[1:], start=1):
    if nr_arg == 0:
        print(f"{nr_arg} arguments.")
    elif nr_arg == 1:
        print(f"{nr_arg} argument:")
        print(f"{index}: {argument}")
    elif nr_arg != 0:
        print(f"{nr_arg} arguments:")
        print(f"{index}: {argument}")