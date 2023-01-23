#!/usr/bin/python3
''' function that finds the biggest integer of a list'''


def max_integer(my_list=[]):
    if my_list == []:
        return None
    jax = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > jax:
            jax = my_list[i]
    return jax
