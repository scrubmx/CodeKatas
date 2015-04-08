#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from ..src import string_calculator

import unittest

class TestStringCalculator(unittest.TestCase):

	def setUp(self):
		self.stringCalculator = string_calculator.StringCalculator()

	def test_returns_zero_with_empty_string(self):
		self.assertEqual(0, self.stringCalculator.compute(""))

	def test_returns_one_with_string_one(self):
		self.assertEqual(1, self.stringCalculator.compute("1"))

	def test_returns_two_with_string_two(self):
		self.assertEqual(2, self.stringCalculator.compute("2"))

	def test_returns_the_sum_of_two_comma_separated_numbers(self):
		self.assertEqual(3, self.stringCalculator.compute("1,2"))

	def test_returns_the_sum_of_two_comma_separated_numbers(self):
		self.assertEqual(10, self.stringCalculator.compute("4,6"))

	def test_returns_the_sum_of_any_number_of_comma_separated_numbers(self):
		self.assertEqual(12, self.stringCalculator.compute("1,2,3,6"))

	def test_returns_the_sum_of_any_number_of_comma_separated_numbers(self):
		self.assertEqual(50, self.stringCalculator.compute("5,25,20"))

	def test_accepts_newLine_character(self):
		self.assertEqual(6, self.stringCalculator.compute("1\n2,3"))

	def test_accepts_any_delimiter_character(self):
		self.assertEqual(3, self.stringCalculator.compute("//;\n1;2"))
		self.assertEqual(11, self.stringCalculator.compute("//;\n1;2;3\n5"))


	def test_it_throws_an_exception_on_negative_numbers(self):
		with self.assertRaises(ValueError):
			self.stringCalculator.compute("-1")
		with self.assertRaises(ValueError):
			self.stringCalculator.compute("-1,-2")

	def test_it_throws_an_exception_with_mixed_numbers(self):
		with self.assertRaises(ValueError):
			self.stringCalculator.compute("-1,3\n2,5")

	def test_it_throws_an_exception_with_mixed_numbers(self):
		try:
			self.stringCalculator.compute("-1,-2")
		except ValueError as error:
			self.assertEqual("-1,-2 is not allowed", error.message)

