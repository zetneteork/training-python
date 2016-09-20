#!/usr/bin/python
# encoding: utf-8

from __future__ import print_function

if __name__ == '__main__':
    texts = {}
    with open("file.txt") as stream:
        for line in stream:
            # Comment or empty line
            if line.startswith("#") or line.startswith("\n"):
                continue
            # Data line
            lang, text = line.split(":", 1)
            texts[lang.strip()] = text.strip()
    print(texts)
