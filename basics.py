#!/usr/bin/env python
# -*- coding: utf-8 -*-

def potenz(b, e=2):
	'''
		Gibt die Lösung zu b hoch e zurück.
		
		Exponentenangabe optional. default ist hoch 2
	'''
	return b**e

def tuplebuilder(*args):
	return args

def dictbuilder(**kwargs):
	return kwargs

if __name__ == '__main__':
	# nützlich wenn libraries auch direkt aufgerufen werden können
	#
	# Alles Folgende wird nur ausgeführt wenn modul direkt (von der Kommandozeile)
	#  aufgerufen wirdm, nicht aber bei einem import.
	#  Alles außerhalb wird auch bei imports aufgerufen.
	pass
	