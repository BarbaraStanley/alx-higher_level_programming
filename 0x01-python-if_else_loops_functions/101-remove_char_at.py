#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str

    new = ""
    for i in range(len(str)):
        if str[i] != str[n]:
            new = new + str[i]
    return new
