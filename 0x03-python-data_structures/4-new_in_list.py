#!/usr/bin/python3
''' replaces an element in a list at a given index without modifying list'''


def new_in_list(my_list, idx, element):
    new = []
    for i in my_list:
        new.append(i)
    if idx >= 0 and idx < len(my_list):
        new[idx] = element
    return new
