#!/usr/bin/python3
def no_c(my_string):
    c = ''
    new_str = [c for c in my_string if c != 'C' and c != 'c']
    return ''.join(new_str)
