# -*- coding: utf-8 -*-

import unittest

class TestMapFilter(unittest.TestCase):

	def test_filter(self):
		"""tests build in filter function

		filter(function, sequence) returns a sequence consisting of those items 
		from the sequence for which function(item) is true. If sequence is a 
		str, unicode or tuple, the result will be of the same type; 
		otherwise, it is always a list.
		"""

		numbers = range(1, 10)
		filtered = filter(lambda x : x < 5, numbers)
		self.assertEqual(list(filtered), [1, 2, 3, 4])

	def test_map(self):
		"""tests build in map function

		map(function, sequence) calls function(item) for each of the sequence’s 
		items and returns a list of the return values.
		"""

		numbers = range(1, 10)
		mapped = map(lambda x : x**2, numbers)
		self.assertEqual(list(mapped), [1,4,9,16,25,36,49,64,81])

if __name__ == '__main__':
	unittest.main()	
