#!/usr/bin/python3
'''reading text file'''


def append_write(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return len(text)
