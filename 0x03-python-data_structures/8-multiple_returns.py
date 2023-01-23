#!/usr/bin/python3
''' function that returns a tuple with length of a string, its 1st character'''


def multiple_returns(sentence):
    if sentence == '':
        return (len(sentence), None)
    return (len(sentence), sentence[0])
