#!/usr/bin/python3
for i in range(0,10):
    for a in range(0, 10):
        if a > i:
            print("{}{}".format(i,a), end=', ')
