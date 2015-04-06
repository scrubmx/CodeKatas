#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

class Integer:

	def __init__(self, number):
		self.number = abs(int(number))

	def is_prime(self):
		# zero and one are not prime numbers
		if self.number < 2: return False

		# all other even numbers are not primes
		if self.number != 2 and self.number % 2 == 0: return False

		count_divisors = 0

		for divisor in range(2, self.number+1):
			if self.number % divisor == 0 : count_divisors += 1

		return count_divisors <= 1

	def get_smallest_divisor(self):
		for divisor in range(2, self.number+1):
			if self.number % divisor == 0: return divisor

	def divide(self, dividend):
		return abs(int(self.number / dividend))

	def value(self):
		return self.number
