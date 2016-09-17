#!/usr/bin/python3
# encoding: utf-8
import unittest
import roman

known_numerals = (
    ('I', 1),
    ('II', 2),
    ('III', 3),
    ('IV', 4),
    ('V', 5),
    ('VI', 6),
    ('IX', 9),
    ('X', 10),
    ('XI', 11),
    ('XVIII', 18),
    ('MMMDCCCLXXXVIII', 3888),
    ('MMMCMXCIX', 3999),
    ('MIX', 1009),
)
correct_numerals = ('I', 'V', 'IV')
incorrect_numerals = ('IIII', 'VIV', 'IVI', 'B', 'MMMM', '0', '1', 'IM', 'CIVIL', 'DIM', 'VIXI', 'XIVI', 'VLIV', 'CIL', 'MIC')

class IsRoman(unittest.TestCase):
    def test_correct_numerals(self):
        """Roman.is_roman_numeral should return True for correct roman numerals."""
        for numeral in correct_numerals:
            self.assertTrue(roman.Roman.is_roman_numeral(numeral),
                msg="'{0}' is not an incorrect numeral.".format(numeral))

    def test_incorrect_numerals(self):
        """Roman.is_roman_numeral should return False for strings that are not roman numerals."""
        for numeral in incorrect_numerals:
            self.assertFalse(roman.Roman.is_roman_numeral(numeral),
                msg="'{0}' is a correct numeral.".format(numeral))

    def test_empty(self):
        self.assertFalse(roman.Roman.is_roman_numeral(''))

    def test_bad_type(self):
        """Roman.is_roman_numeral should raise TypeError for non-string arguments"""
        for numeral in (None, 0, 1, 1.0):
            self.assertRaises(TypeError, roman.Roman.is_roman_numeral, numeral)

class FromInteger(unittest.TestCase):
    def test_known_numerals(self):
        """Roman(integer) makes a correct numeral."""
        for numeral, value in known_numerals:
            self.assertEqual(str(roman.Roman(value)), numeral)

class ToInteger(unittest.TestCase):
    def test_known_numerals(self):
        """Roman(numeral) converts to the right integer."""
        for numeral, value in known_numerals:
            self.assertEqual(int(roman.Roman(numeral)), value)

class Inversion(unittest.TestCase):
    def test_inversion(self):
        for i in range(1, 4000):
            self.assertEqual(int(roman.Roman(i)), i)

if __name__ == '__main__':
    unittest.main()
