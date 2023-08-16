#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_key = None
    best_num = float('-inf')

    for key, value in a_dictionary.items():
        if value > best_num:
            best_key = key
            best_num = value

    return best_key
