#!/usr/bin/python3

def best_score(a_dictionary):
    
    if a_dictionary is None:
        return None

    h_key = None
    h_value = float('-inf')
    for key, value in a_dictionary.items():
        if value > h_value:
            h_key = key
            h_value = value
    return h_key
