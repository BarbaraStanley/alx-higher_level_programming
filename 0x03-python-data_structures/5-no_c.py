#!/usr/bin/python3
''' function that removes all characters c and C from a string '''


def no_c(my_string):
    rem = ['c', 'C']
    new_s = []
    for i in my_string:
        if i in rem:
            i = ''
        new_s.append(i)
    return ''.join(new_s)
