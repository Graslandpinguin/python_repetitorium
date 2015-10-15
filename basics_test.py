#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class TestBasicLanguageFeatures(unittest.TestCase):

	def setUp(self):
		"""
			wird vor jedem einzellnen test ausgeführt

			hier am besten datensätze vorbereiten, externe verbindungen aufbauen, etc
		"""

		print("Setting up test case")

	def tearDown(self):
		"""
			wird nach jedem einzellnen test ausgeführt

			hier am besten Verbindungen schließen etc
		"""

		print("Tearing down test case")

	def test_stringFormat(self):
		a = "H{0}llo {1}".format('a', 23423)

		self.assertEqual(a, "Hallo 23423")

		b = [str(i) for i in range(1,5)]
		# liste von strings zusammenfügen mit seperator
		b_str = ">".join(b)
		self.assertEqual(b_str, "1>2>3>4")
		
	def test_kontrollfluss(self):
		result = ""
		p = 11
		if p < 20:
			result = "p < 20"
		elif 20 <= p < 50: 
			result = "p < 50"
		else:
			result = "p >= 50"
		self.assertEqual(result, "p < 20")

		result = []
		for i in range(3,10,2):
			result.append(i)
		self.assertEqual(result, [3,5,7,9])

		result = []
		for i in ["a", 3, 3.3]:
			result.append(i)
		self.assertEqual(result, ["a", 3, 3.3])

		result = ""
		for i, v in enumerate(['tic', 'tac', 'toe']):
			result += "{}:{}, ".format(i, v)
		self.assertEqual(result, "0:tic, 1:tac, 2:toe, ")

		j = 0
		while j < 10:
			print(j)
			j += 3
		self.assertEqual(j, 12)

	def test_exceptions(self):
		
		zahl_gefunden = False
		while not zahl_gefunden:
			try:
				# reading something from standard input
				# raw_input gibts nicht mehr seit 3.x ..
				gewaehlte_zahl = int(input("Hier eine Zahl eingeben: "))

				if gewaehlte_zahl < 10:
					raise ValueError("zwar eine Zahl, aber zu niedrig.")
				
			except ValueError as e:
				# wird ausgeführt, wenn ein ValueError auftritt
				
				print("exception block {}".format(type(e)))
				#print(e.args)
				print(e)
				print("Das war leider nichts.")

				# gib die Exception zusätzlich weiter eine Ebene nach oben. 
				# Nicht gebraucht, wenn Exception wirklich *behandelt* wird
				#raise e
			except Exception as e:
				# wird ausgeführt, wenn irgendein anderer Exception-Typ auftritt
				
				print("exception block {}".format(type(e)))
				#print(e.args)
				print(e)
			else:
				# wird nur ausgeführt wenn try block keine Exceptions wirft
				
				print("else block")
				zahl_gefunden = True
				print(gewaehlte_zahl)
			finally:
				# wird immer am Ende ausgeführt egal ob es eine Exception gab oder nicht
				# hier cleanup Sachen
				
				print("finally block")

	def test_multiple_args_listbuilder(self):
		def tuplebuilder(*args):
			"""A function can be called with an arbitrary number of arguments. 
				These arguments will be wrapped up in a tuple.
			"""
			return args

		result = tuplebuilder(1,2,3,4,5)
		self.assertEqual(result, (1,2,3,4,5))
		result = tuplebuilder(3,[4])
		self.assertEqual(result, (3,[4]))

	def test_multiple_kwars_dictbuilder(self):
		def dictbuilder(**kwargs):
			return kwargs

		result = dictbuilder(a=1, b=2, c=3, d=4)
		self.assertEqual(result, {"a" : 1, "b" : 2, "c" : 3, "d" : 4})
		result = dictbuilder(a=1, d=4)
		self.assertEqual(result, {"a" : 1, "d" : 4})

	def test_multi_line_string_split(self):
		pass

	def test_lambda_func(self):
		pass

if __name__ == '__main__':
	# nützlich wenn libraries auch direkt aufgerufen werden können
	#
	# Alles Folgende wird nur ausgeführt wenn modul direkt (von der Kommandozeile)
	#  aufgerufen wirdm, nicht aber bei einem import.
	#  Alles außerhalb wird auch bei imports aufgerufen.

    unittest.main()