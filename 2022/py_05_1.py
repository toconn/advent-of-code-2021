#!/usr/bin/env python3

from py_shared import *
from dataclasses import dataclass

DAY = 5
PART = 1;

# Types ────────────────────────────────────────────────────────────────────── #

@dataclass
class Move:
	count: int
	source: int
	target: int

# Solution ─────────────────────────────────────────────────────────────────── #

def solve(lines):

	stacks = to_stacks(lines)
	moves = to_moves(lines)
	return ''.join(solve_moves(stacks, moves))

def solve_moves(stacks, moves):

	print(stacks)

	for move in moves:

		crates = []

		for i in range(move.count):
			crates.append(stacks[move.source].pop())

		for i in range(move.count):
			stacks[move.target].append(crates.pop(0))

	return [stack[-1] for stack in stacks]

def is_move(line):
	return line.startswith("move")

def is_stack(line):
	return not_blank(line) and line

def reverse(items):
	reversed = items.copy()
	reversed.reverse()
	return reversed
	
def to_move(line):
	parts = line.split()
	return Move(int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1)

def to_moves(lines):
	return [to_move(line) for line in lines if is_move(line)]

def stack_crates(stacks, line):

	for index in range(len(stacks)):
		letter = line[1 + index * 4]
		if not_blank(letter):
			stacks[index].append(letter)

def to_stacks(lines):

	stacks = []

	for line in reverse(lines):

		if is_blank(line) or is_move(line):
			continue

		if line.startswith(' 1'):
			count = int(line.split()[-1])
			for i in range(count):
				stacks.append([])
			continue

		stack_crates(stacks, line)

	return stacks

# Main ─────────────────────────────────────────────────────────────────────── #

# run_test(DAY, PART, solve)
run_test_and_actual(DAY, PART, solve)
