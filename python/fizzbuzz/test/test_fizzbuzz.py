#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from ..src import fizzbuzz

import unittest

class TestFizzBuzz(unittest.TestCase):

	def setUp(self):
		self.fizzbuzz = fizzbuzz.FizzBuzz()

	def test_it_returns_1_for_input_1(self):
		self.assertEqual("1", self.fizzbuzz.convert(1))

	def test_it_returns_2_for_input_2(self):
		self.assertEqual("2", self.fizzbuzz.convert(2))

	def test_it_returns_fizz_for_input_3(self):
		self.assertEqual("fizz", self.fizzbuzz.convert(3))

	def test_it_returns_buzz_for_input_5(self):
		self.assertEqual("buzz", self.fizzbuzz.convert(5))

	def test_it_returns_buzz_for_input_6(self):
		self.assertEqual("fizz", self.fizzbuzz.convert(6))

	def test_it_returns_buzz_for_input_15(self):
		self.assertEqual("fizzbuzz", self.fizzbuzz.convert(15))

	def test_it_returns_buzz_for_input_30(self):
		self.assertEqual("fizzbuzz", self.fizzbuzz.convert(30))

	def test_it_throws_an_exception_when_given_invalid_input(self):
		with self.assertRaises(ValueError):
			self.fizzbuzz.convert("INVALID")
