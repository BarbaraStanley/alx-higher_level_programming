#!/usr/bin/python3
''' A function that indents a text after '.','?' or ':' '''


def text_indentation(text):
    '''prints a text with 2 new lines after each of: ., ? and : '''
    if type(text) is not str:
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    for s in characters:
        comp = [line.strip() for line in text.split(s)]
        text = (s + "\n\n\n").join(comp)
    print(text, end='')
