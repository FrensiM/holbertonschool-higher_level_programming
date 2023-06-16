#!/usr/bin/python3
"""Print square module"""


def text_indentation(text):
    """Print square module"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    char = [".", "?", ":"]
    el = 0
    while el < len(text):
        print(f"{text[el]}", end="")
        if text[el] in char:
            print()
            print()
            while el + 1 <= len(text) and text[el + 1] == " ":
                el += 1
        el += 1
