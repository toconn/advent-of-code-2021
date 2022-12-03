#!/usr/bin/env python3

from shared import *
from day_03_data import *

# Solution ─────────────────────────────────────────────────────────────────── #

def calculate(data):

	answer = 0
	for first, second, third in every_3_lines(to_lines(data)):
		answer += score_duplicate(first, second, third)
	return answer

def every_3_lines(lines):
	for i in range(0, len(lines), 3):
		yield lines[i], lines[i+1], lines[i+2]

def has_letter(line, letter):
	return line.find(letter) >= 0

def score(letter):
	return ord(letter) - (96 if letter > 'Z' else 38)

def score_duplicate(first, second, third):
	for letter in first:
		if has_letter(second, letter) and has_letter(third, letter):
			return score(letter)


# Main ─────────────────────────────────────────────────────────────────────── #

def run():
	print ("Answer:", calculate(DATA_1))
	

def test():
	answer = calculate(TEST)
	print ("Test:", answer, "👍" if answer == TEST_ANSWER_2 else f'(≠ {TEST_ANSWER_2}) ❌')


run()
# test()
