#!/usr/bin/bash
def uniq_add(my_list=[]):
    sum = 0
    my_set = set(my_list)
    for i in my_set:
        sum = sum + i
    return (sum)
