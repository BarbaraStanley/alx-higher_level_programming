#!/usr/bin/python3
''' replaces an element in a list at a given index without modifying list'''


def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        new = []
        for i in my_list:
            new.append(i)
        new[idx] = element
    return new
