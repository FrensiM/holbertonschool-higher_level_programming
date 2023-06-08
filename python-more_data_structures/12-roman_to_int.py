#!/usr/bin/python3
def roman_to_int(roman_string):
    dict1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    dict2 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    total = 0
    i = 0
    if roman_string is None or type(roman_string) != str:
        return total
    while i < len(roman_string):
        sub = roman_string[i: i + 2]
        if sub in dict2:
            total += dict2[sub]
            i += 2
        elif roman_string[i] in dict1:
            total += dict1[roman_string[i]]
            i += 1
    return total
