#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from . import math

class PrimeFactors:

	def __init__(self):
		self.result = []

	def calculate(self, number):

		# make sure the number is a positive integer
		integer = math.Integer(number)

		# if the number is prime that means we can't divide further
		# when that's the case we just append the number to the list and return.
		if integer.is_prime():
			self.result.append(integer.value())
			return self.result

		# if the number is not prime then find the lowest posible dividend
		# and append it to the result list
		divisor = integer.get_smallest_divisor()
		self.result.append(divisor)

		# finally we call `self.calculate` recursively until we are done.
		return self.calculate(integer.divide(divisor))
