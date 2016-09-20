#!/usr/bin/python

from __future__ import print_function

import sys


def write_file(filename):
    with open(filename, "w") as stream:
        print("#", file=stream)
        print("# Hello in a few languages", file=stream)
        print("#", file=stream)
        print("", file=stream)
        print("en:", "Hello!", file=stream)
        print("cs:", "Dobrý den!", file=stream)
        print("sk:", "Dobrý deň!", file=stream)
        print("pl:", "Dzień dobry!", file=stream)
        print("it:", "Buon giorno!", file=stream)
        print("ru:", "Добрый день!", file=stream)


def read_file(filename):
    texts = {}
    with open(filename) as stream:
        for line in stream:
            # Comment or empty line
            if line.startswith("#") or line.startswith("\n"):
                continue
            # Missing colon
            if ':' not in line:
                raise ValueError("Invalid line: {!r}".format(line))
            # Data line
            lang, text = line.split(":", 1)
            texts[lang.strip()] = text.strip()
    return texts


def usage():
    sys.exit("Usage: {} read|write".format(sys.argv[0]))


def main():
    try:
        command = sys.argv[1]
    except IndexError:
        usage()

    if command == "write":
        write_file("file.txt")
    elif command == "read":
        try:
            data = read_file("file.txt")
        except FileNotFoundError as e:
            sys.exit(e)
        print(data)
    else:
        usage()


if __name__ == '__main__':
    main()
