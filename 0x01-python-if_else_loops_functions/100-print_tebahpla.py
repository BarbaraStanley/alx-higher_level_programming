#!/usr/bin/python3
a = 0
for i in range(ord('z'), ord('a') -1, -1):
    print("{}".format(chr(i - a)), end="")
    i = 32 if i == 0 else 0
