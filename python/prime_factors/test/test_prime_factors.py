#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ..src import prime_factors

import unittest

class TestPrimeFactors(unittest.TestCase):

	def setUp(self):
		self.prime_factors = prime_factors.PrimeFactors()

	def test_it_returns_2_for_2(self):
		self.assertEqual([2], self.prime_factors.calculate(2))

	def test_it_returns_3_for_3(self):
		self.assertEqual([3], self.prime_factors.calculate(3))

	def test_it_returns_2_2_for_4(self):
		self.assertEqual([2, 2], self.prime_factors.calculate(4))
		self.prime_factors.calculate

	def test_it_returns_5_for_5(self):
		self.assertEqual([5], self.prime_factors.calculate(5))

	def test_it_returns_2_3_for_6(self):
		self.assertEqual([2, 3], self.prime_factors.calculate(6))

	def test_it_returns_7_for_7(self):
		self.assertEqual([7], self.prime_factors.calculate(7))

	def test_it_returns_2_2_2_for_8(self):
		self.assertEqual([2, 2, 2], self.prime_factors.calculate(8))

	def test_it_returns_3_3_for_9(self):
		self.assertEqual([3, 3], self.prime_factors.calculate(9))

	def test_it_returns_2_5_for_10(self):
		self.assertEqual([2, 5], self.prime_factors.calculate(10))

	def test_it_returns_11_for_11(self):
		self.assertEqual([11], self.prime_factors.calculate(11))

	def test_it_returns_2_2_3_for_12(self):
		self.assertEqual([2, 2, 3], self.prime_factors.calculate(12))

	def test_it_returns_13_for_13(self):
		self.assertEqual([13], self.prime_factors.calculate(13))

	def test_it_returns_2_7_for_14(self):
		self.assertEqual([2, 7], self.prime_factors.calculate(14))

	def test_it_returns_3_5_for_15(self):
		self.assertEqual([3, 5], self.prime_factors.calculate(15))

	def test_it_returns_2_2_2_2_for_16(self):
		self.assertEqual([2, 2, 2, 2], self.prime_factors.calculate(16))

	def test_it_returns_17_for_17(self):
		self.assertEqual([17], self.prime_factors.calculate(17))

	def test_it_returns_2_3_3_for_18(self):
		self.assertEqual([2, 3, 3], self.prime_factors.calculate(18))

	def test_it_returns_19_for_19(self):
		self.assertEqual([19], self.prime_factors.calculate(19))

	def test_it_returns_2_2_5_for_20(self):
		self.assertEqual([2, 2, 5], self.prime_factors.calculate(20))

	def test_it_returns_2_2_5_5_for_100(self):
		self.assertEqual([2, 2, 5, 5], self.prime_factors.calculate(100))

	def test_it_returns_5_5_37_for_555(self):
		self.assertEqual([3, 5, 37], self.prime_factors.calculate(555))
