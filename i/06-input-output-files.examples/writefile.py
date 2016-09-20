#!/usr/bin/python
# encoding: utf-8

from __future__ import print_function

if __name__ == '__main__':
    with open("file.txt", "w") as stream:
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
