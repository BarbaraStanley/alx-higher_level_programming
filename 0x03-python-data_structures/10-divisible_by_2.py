#!/usr/bin/python3
''' function that finds all multiples of 2 in a list '''


def divisible_by_2(my_list=[]):
    tf_list = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            tf_list.append(True)
        else:
            tf_list.append(False)
    return tf_list
