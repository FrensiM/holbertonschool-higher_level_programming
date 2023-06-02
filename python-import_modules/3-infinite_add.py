#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = 1
    sum = 0
    while i < len(sys.argv):
        sum += int(sys.argv[i])
        i += 1
    print(f"{sum}")
