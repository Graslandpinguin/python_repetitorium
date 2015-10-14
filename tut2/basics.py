#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("-----------Printing-----------")


# printing something to standard output
print("Something")

#for objects you have to convert explicitly to string: str(obj)
print("H{0}llo {1}".format('a', 23423))

print("-----------Kontrollfluss-----------")
print()

p = 11
if p < 20:
	print("p < 20")
elif 20 <= p < 50: 
	print("p < 50")
else:
	print("p nothing")

print()

for i in range(0,10,2):
	print(i)

print()

liste = ["a", 3, 3.3]
for i in liste:
	print(i)

print()

j = 1
while j < 10:
	print(j)
	j += 3


print("-----------Exceptions-----------")

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
