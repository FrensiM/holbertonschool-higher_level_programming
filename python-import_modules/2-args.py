#!/usr/bin/python3
import sys
if __name__ == "__main__":
    nr_arg = len(sys.argv) - 1
if nr_arg == 0:
    print(f"{nr_arg} arguments.")
elif nr_arg == 1:
    print(f"{nr_arg} argument:")
else:
    print(f"{nr_arg} arguments:")
for index, arg in enumerate(sys.argv[1:], start=1):
    print(f"{index}: {sys.argv[index]}")    