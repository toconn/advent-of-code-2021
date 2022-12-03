#!/usr/bin/env python3

from shared import *
from day_03_data import *

# Solution ─────────────────────────────────────────────────────────────────── #

def calculate(data):

	answer = 0
	for line in to_lines(data):
		answer += score_duplicate(line)
	return answer

def score(letter):
	return ord(letter) - (96 if letter > 'Z' else 38)

def score_duplicate(line):

	split = len(line)//2
	first, second = line[:split], line[split:]

	for letter in first:
		if second.find(letter) >= 0:
			return score(letter)

	print ("  Not found", line, first, second)
	nl()

# Main ─────────────────────────────────────────────────────────────────────── #

def run():
	print ("Answer:", calculate(DATA_1))
	
def test():
	answer = calculate(TEST)
	print ("Test:", answer, "👍" if answer == TEST_ANSWER_1 else f'(≠ {TEST_ANSWER_1}) ❌')


run()
# test()
