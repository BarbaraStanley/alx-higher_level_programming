#!/usr/bin/python3
'''A function that reads a text file and prints to stdout'''


def read_file(filename=""):
    ''' Reads a file specified by the user and prints the content to stdout'''
    with open(filename, encoding="utf-8") as aFile:
        print(aFile.read(), end='')
