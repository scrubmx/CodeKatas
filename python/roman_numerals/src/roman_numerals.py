#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division

class RomanNumeralsConverter(object):

	romans_dict = {
		1000 : 'M',
		900  : 'CM',
		500  : 'D',
		400  : 'CD',
		100  : 'C',
		90   : 'XC',
		50   : 'L',
		40   : 'XL',
		10   : 'X',
		9    : 'IX',
		5    : 'V',
		4    : 'IV',
		1    : 'I',
	}

	def __init__(self):
		self.result = ''

	def convert(self, number):

		keys = self.romans_dict.keys()
		Keys = keys.sort(reverse=True)

		for key in keys:
			while number >= key:
				self.result += self.romans_dict[key]
				number -= key

		return self.result