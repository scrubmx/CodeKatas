#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division
from ..src import roman_numerals

import unittest

class TestRomanNumerals(unittest.TestCase):

	def setUp(self):
		self.roman_numerals = roman_numerals.RomanNumeralsConverter()

	def test_it_calculates_the_roman_numeral_for_1(self):
		self.assertEqual('I', self.roman_numerals.convert(1))

	def test_it_calculates_the_roman_numeral_for_2(self):
		self.assertEqual('II', self.roman_numerals.convert(2))

	def test_it_calculates_the_roman_numeral_for_3(self):
		self.assertEqual('III', self.roman_numerals.convert(3))

	def test_it_calculates_the_roman_numeral_for_4(self):
		self.assertEqual('IV', self.roman_numerals.convert(4))

	def test_it_calculates_the_roman_numeral_for_5(self):
		self.assertEqual('V', self.roman_numerals.convert(5))

	def test_it_calculates_the_roman_numeral_for_6(self):
		self.assertEqual('VI', self.roman_numerals.convert(6))

	def test_it_calculates_the_roman_numeral_for_7(self):
		self.assertEqual('VII', self.roman_numerals.convert(7))

	def test_it_calculates_the_roman_numeral_for_8(self):
		self.assertEqual('VIII', self.roman_numerals.convert(8))

	def test_it_calculates_the_roman_numeral_for_9(self):
		self.assertEqual('IX', self.roman_numerals.convert(9))

	def test_it_calculates_the_roman_numeral_for_10(self):
		self.assertEqual('X', self.roman_numerals.convert(10))

	def test_it_calculates_the_roman_numeral_for_11(self):
		self.assertEqual('XI', self.roman_numerals.convert(11))

	def test_it_calculates_the_roman_numeral_for_20(self):
		self.assertEqual('XX', self.roman_numerals.convert(20))

	def test_it_calculates_the_roman_numeral_for_45(self):
		self.assertEqual('XLV', self.roman_numerals.convert(45))

	def test_it_calculates_the_roman_numeral_for_50(self):
		self.assertEqual('L', self.roman_numerals.convert(50))

	def test_it_calculates_the_roman_numeral_for_100(self):
		self.assertEqual('C', self.roman_numerals.convert(100))

	def test_it_calculates_the_roman_numeral_for_500(self):
		self.assertEqual('D', self.roman_numerals.convert(500))

	def test_it_calculates_the_roman_numeral_for_1000(self):
		self.assertEqual('M', self.roman_numerals.convert(1000))

	def test_it_calculates_the_roman_numeral_for_1494(self):
		self.assertEqual('MCDXCIV', self.roman_numerals.convert(1494))

	def test_it_calculates_the_roman_numeral_for_1999(self):
		self.assertEqual('MCMXCIX', self.roman_numerals.convert(1999))

	def test_it_calculates_the_roman_numeral_for_4990(self):
		self.assertEqual('MMMMCMXC', self.roman_numerals.convert(4990))
