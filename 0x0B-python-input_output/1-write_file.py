#!/usr/bin/python3
''' a function that writes a string to a text file (UTF8),
    and returns the number of characters written '''


def write_file(filename="", text=""):
    ''' appends text to filename, and creates filename if it doesn't exist'''
    with open(filename, mode="x", encoding="utf-8") as new:
        length = new.write(text)
    return (length)
