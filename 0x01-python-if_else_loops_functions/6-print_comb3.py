#!/usr/bin/python3
for i in range(0, 10):
    for a in range(0, 10):
        if a > i:
            if i != 8:
                print("{}{}".format(i, a), end=', ')
print("{}".format(89))
