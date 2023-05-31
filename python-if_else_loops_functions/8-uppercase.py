#!/usr/bin/python3
def uppercase(str):
    new = ""
    for ch in str:
        val = ord(ch)
        if val >= 97 and val <= 122:
            new = new + chr(val - 32)
        else:
            new += ch
    print("{}".format(new))
