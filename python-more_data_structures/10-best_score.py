#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_key = None
    first = True
    for key in a_dictionary:
        if first is True:
            max_key = key
            first = False
        if a_dictionary[key] > a_dictionary[max_key]:
            max_key = key
    return max_key