#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ..src import math

import unittest

class TestInteger(unittest.TestCase):

	def test_it_can_check_if_number_is_prime(self):
		self.assertTrue(math.Integer(2).is_prime())
		self.assertTrue(math.Integer(7).is_prime())

	def test_it_can_divide_two_numbers(self):
		self.assertEquals(5, math.Integer(10).divide(2))
		self.assertEquals(20, math.Integer(100).divide(5))

	def test_it_can_get_the_smallest_divisor_for_the_number(self):
		self.assertEquals(2, math.Integer(4).get_smallest_divisor())
		self.assertEquals(3, math.Integer(15).get_smallest_divisor())
		self.assertEquals(5, math.Integer(25).get_smallest_divisor())
