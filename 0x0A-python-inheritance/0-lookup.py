#!/usr/bin/bash
''' A function that returns the list of available attributes
and methods of an object'''


def lookup(obj):
    ''' Returns list of attributes and methods of an object'''
    return dir(obj)
