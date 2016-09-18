#!/usr/bin/python

from __future__ import print_function

if __name__ == '__main__':
    with open("file.txt", "w") as stream:
        print("en:", "Hello!", file=stream)
        print("cs:", "Dobrý den!", file=stream)
        print("sk:", "Dobrý deň!", file=stream)
        print("pl:", "Dzień dobry!", file=stream)
