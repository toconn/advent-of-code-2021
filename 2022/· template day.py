#!/usr/bin/env python3

from shared import *
from dataclasses import dataclass

from day_%day%_data import *

# Types ────────────────────────────────────────────────────────────────────── #

@dataclass
class xxx:
	pass


# Solution ─────────────────────────────────────────────────────────────────── #

def calculate(data):
	answer = 0
	for line in to_lines(data):
		pass
	return answer


# Main ─────────────────────────────────────────────────────────────────────── #

def run():
	print ("Answer:", calculate(DATA_1))
	

def test():
	answer = calculate(TEST)
	print ("Test:", answer, "👍" if answer == TEST_ANSWER_%part% else f'(≠ {TEST_ANSWER_%part%}) ❌')


# run()
test()
