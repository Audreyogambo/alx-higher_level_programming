#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    clone = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return clone
    clone[idx] = element
    return 