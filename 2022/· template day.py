#!/usr/bin/env python3

from shared import *
from dataclasses import dataclass

from day_data import *

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

def test():
	answer = calculate(TEST)
	print ("Test:", answer, "👍" if answer == TEST_ANSWER_1 else f'(≠ {TEST_ANSWER_1}) ❌')


# print ("Answer:", calculate(DATA_1))
test()
