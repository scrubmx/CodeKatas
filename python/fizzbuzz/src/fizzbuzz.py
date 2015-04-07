#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

class FizzBuzz:

	def convert(self, number):

		# throws an exception if can convert
		number = int(number)

		result = ""

		if number % 3 == 0:
			result = "fizz"
		if number % 5 == 0:
			result += "buzz"
		if result == "":
			result = str(number)

		return result

	def display(self):
		for x in range(1, 101):
			print self.convert(x)
