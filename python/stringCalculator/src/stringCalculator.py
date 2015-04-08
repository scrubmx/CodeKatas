#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

class StringCalculator:

	delimiter = ","

	def compute(self, str):

		if str == "":
			return 0

		if "-" in str:
			raise ValueError(str+" is not allowed")

		if str[0] == "/" and str[1] == "/":
			self.delimiter = str[2]
			str = str[4:len(str)]

		strList = str.split("\n")
		retval = 0
		for partOfString in strList:
			retval += self.sum(partOfString)
		return retval


		

	def sum(self, str):

		pieces = str.split(self.delimiter)

		return sum(int(i) for i in pieces)
