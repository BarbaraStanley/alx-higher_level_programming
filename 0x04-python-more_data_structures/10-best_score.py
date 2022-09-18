#!/usr/bin/python3
def best_score(a_dictionary):
    makelist = list(a_dictionary.items())
    max_value = makelist[0][1]
    key = makelist[0][0]
    for i in range(len(makelist):
        if makelist[i][1] > max_value:
            max_value = makelist[i][1]
            key = makelist[i][0]
    return (key)

