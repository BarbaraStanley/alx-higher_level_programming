#!/usr/bin/python3

import sys

sum = 0
num = len(sys.argv)
if num == 1:
    sum = 0
else:
    for i in range(1, num):
        sum += int(sys.argv[i])
    print("{}".format(sum))
