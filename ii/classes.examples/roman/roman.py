# encoding: utf-8
"""A library for using and converting roman numbers

"""
from __future__ import print_function
import re
import sys

if sys.version_info.major == 2:
    input = raw_input

ROMAN_NUMERAL_REGEX_STRING = r"""
^                   # beginning of string
M{0,3}              # thousands: 0, M, MM, MMM
(D?C{0,3}|C?D|CM)   # hundreds: 0, C, CC, CCC, CD, D, DC, DCC, DCCC, CM
(L?X{0,3}|X?L|XC)   # tens: 0, X, XX, XXX, XL, L, LX, LXX, LXXX, XC
(V?I{0,3}|I?V|IX)   # units: 0, I, II, III, IV, V, VI, VII, VIII, IX
$                   # end of string
"""

DIGITS = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
]

class Roman(object):
    """A roman number"""
    _roman_numeral_regex = re.compile(ROMAN_NUMERAL_REGEX_STRING, re.VERBOSE)

    @classmethod
    def is_roman_numeral(cls, numeral):
        """Check a string whether it is a roman numeral"""
        if numeral == '':
            return False
        return bool(cls._roman_numeral_regex.match(numeral))

    def __init__(self, obj):
        if (isinstance(obj, str)):
            self._numeral = obj
        elif (isinstance(obj, int)):
            n = obj
            self._numeral = ''
            for digit, value in DIGITS:
                while value <= n:
                    self._numeral += digit
                    n -= value

    def __int__(self):
        n = 0
        i = 0
        for digit, value in DIGITS:
            while self._numeral[i:i+len(digit)] == digit:
                i += len(digit)
                n += value
        return n

    def __str__(self):
        return self._numeral

    def __repr__(self):
        return "Roman('{0}')".format(self._numeral)

    def __add__(self, other):
        return Roman(int(self) + int(other))

if __name__ == '__main__':
    import optparse
    #import argparse
    parser = optparse.OptionParser()
    parser.add_option("-i", "--integer", action="store_true", dest="reverse", help="convert integer to roman")
    parser.add_option("-r", "--roman", action="store_false", dest="reverse", help="convert roman to integer")
    parser.set_defaults(reverse=False)

    options, args = parser.parse_args()

    if len(args) == 1:
        if options.reverse:
            r = Roman(int(args[0]))
        else:
            r = Roman(args[0])
        print("{0} = {1}".format(r, int(r)))
    else:
        print("Usage: roman [-i|--integer|-r|--roman] <arg>", file=sys.stderr)

