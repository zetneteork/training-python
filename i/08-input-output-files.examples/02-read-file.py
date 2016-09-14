#!/usr/bin/python

if __name__ == '__main__':
    with open("file.txt") as stream:
        texts = {}
        for line in stream:
            lang, text = (item.strip() for item in line.split(":", 1))
            texts[lang] = text
