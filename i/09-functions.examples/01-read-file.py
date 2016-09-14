#!/usr/bin/python

from __future__ import print_function

def read_file(filename):
    texts = {}
    with open(filename) as stream:
        for line in stream:
            lang, text = (item.strip() for item in line.split(":", 1))
            texts[lang] = text
    return texts

if __name__ == '__main__':
    texts_by_lang = read_file("file.txt")
    print(texts_by_lang)
