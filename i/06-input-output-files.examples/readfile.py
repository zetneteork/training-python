#!/usr/bin/python

if __name__ == '__main__':
    texts = {}
    with open("file.txt") as stream:
        for line in stream:
            # Empty line
            if not line:
                continue
            # Comment
            if line.startswith("#"):
                continue
            # Data line
            lang, text = (item.strip() for item in line.split(":", 1))
            texts[lang] = text
    print(texts)
