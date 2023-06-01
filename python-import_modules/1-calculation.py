#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    a = 10
    b = 5
print("{} + {} = {}".format(a, b , add(a, b)))
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")