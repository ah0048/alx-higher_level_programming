#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    score = 0
    name = None
    for key, value in a_dictionary.items():
        if score < value:
            score = value
            name = key
    return name
