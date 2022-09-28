#!/usr/bin/python3
''' A function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added'''


def append_write(filename="", text=""):
    ''' appends text to the end of a file, creates file if its nonexistent'''
    with open(filename, mode="a", encoding="utf-8") as appended:
        added_len = appended.write(text)
        return (added_len)
