#!/usr/bin/env python3

from py_shared import *
from dataclasses import dataclass

from py_02_data import *

# A - 1, Rock
# B - 2, Paper
# C - 3, Scissors

# X - 0, Lose
# Y - 3, Draw
# Z - 6, Win

# Score = Shape + Result

# Types ────────────────────────────────────────────────────────────────────── #

@dataclass
class Shape:
	win: str
	lose: str
	score: int

# Data ─────────────────────────────────────────────────────────────────────── #

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

WIN = 'Z'
LOSE = 'X'
DRAW = 'Y'

SHAPES = {
	ROCK: Shape(SCISSORS, PAPER, 1),
	PAPER: Shape(ROCK, SCISSORS, 2),
	SCISSORS: Shape(PAPER, ROCK, 3)
}

# Solution ─────────────────────────────────────────────────────────────────── #

def calculate(data):
	scores = [score_game(game) for game in to_lines(data)]
	return sum(scores)

def score_result(shape_1, shape_2):
	if shape_1 == shape_2:
		return 3
	if SHAPES[shape_2].win == shape_1:
		return 6
	return 0

def score_shape(shape):
	return SHAPES[shape].score

def score_game(game):
	shape_1, shape_2 = to_shapes(game)
	return score_shape(shape_2) + score_result(shape_1, shape_2)

def to_player_2_shape(shape, play):
	if play == WIN:
		return SHAPES[shape].lose
	if play == LOSE:
		return SHAPES[shape].win
	return shape

def to_shapes(game):
	shape_1, play = game.split(' ')
	return shape_1, to_player_2_shape(shape_1, play)

# Main ─────────────────────────────────────────────────────────────────────── #

def test():
	answer = calculate(TEST)
	print ('Test:', answer, '👍' if answer == TEST_ANSWER_2 else f'(≠ {TEST_ANSWER_2}) ❌')


print ('Answer:', calculate(DATA_1))
# test()

