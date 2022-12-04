#!/usr/bin/env python3

from py_shared import *

from py_02_data import *

# A, X - 1, Rock
# B, Y - 2, Paper
# C, Z - 3, Scissors

# Win  - 6
# Lose - 0
# Draw - 3

# Score = Shape + Result

# Solution ─────────────────────────────────────────────────────────────────── #

def calculate(data):
	scores = [score_game(game) for game in to_lines(data)]
	return sum(scores)

def score_result(shape_1, shape_2):
	if shape_1 == shape_2:
		return 3
	if shape_1 == "rock" and shape_2 == "paper":
		return 6
	if shape_1 == "paper" and shape_2 == "scissors":
		return 6
	if shape_1 == "scissors" and shape_2 == "rock":
		return 6
	return 0

def score_shape(shape):
	match shape:
		case "rock":
			return 1
		case "paper":
			return 2
		case "scissors":
			return 3

def score_game(game):
	shape_1, shape_2 = to_shapes(game)
	return score_shape(shape_2) + score_result(shape_1, shape_2)

def to_shape(shape):
	match shape:
		case "A" | "X":
			return "rock"
		case "B" | "Y":
			return "paper"
		case "C" | "Z":
			return "scissors"

def to_shapes(game):
	shape_1, shape_2 = game.split(" ")
	return to_shape(shape_1), to_shape(shape_2)

def test():
	answer = calculate(TEST)
	print ("Test:", answer, "👍" if answer == TEST_ANSWER else f'(≠ {TEST_ANSWER}) ❌')


print ("Answer:", calculate(DATA_1))
# test()

