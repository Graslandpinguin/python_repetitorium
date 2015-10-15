# -*- coding: utf-8 -*-

"""
    Argparse tutorial

    based on https://docs.python.org/3.3/howto/argparse.html
"""

import argparse

parser = argparse.ArgumentParser()

# positional arguments
parser.add_argument("message", help="multiply this message a number of times")
parser.add_argument("times", help="multiply the message by this number", type=int)

# optional argument
parser.add_argument("-v", "--verbosity", help="how verbose the output should be", type=int, default=0, choices=[0, 1, 2])

# optional FLAG
parser.add_argument("-s", "--special", help="activate special output", action="store_true")

args = parser.parse_args()

print("verbositylvl: {}".format(args.verbosity))

print(args.message*args.times)
if args.special:
	print("spezial modus war aktiviert")
