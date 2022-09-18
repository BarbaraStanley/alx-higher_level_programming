#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    else:
        make = list(a_dictionary.items())
        max_value = make[0][1]
        key = make[0][0]

    for i in range(len(make)):
        if make[i][1] > max_value:
            max_value = make[i][1]
            key = make[i][0]
    return key
