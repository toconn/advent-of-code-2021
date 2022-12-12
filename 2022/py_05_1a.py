#!/usr/bin/env python3

from py_shared import *
from dataclasses import dataclass

DAY = 5
PART = 1;

# Types ────────────────────────────────────────────────────────────────────── #

@dataclass
class Instruction:
	count: int
	source: int
	target: int

# Solution ─────────────────────────────────────────────────────────────────── #

def solve(lines):

	stackings, instructions = split_list(lines, is_empty)
	stacks = move_crates(to_stacks(stackings), to_instructions(instructions))
	return ''.join(top_crates(stacks))

def add_crates(stacks, line):

	for index in range(len(stacks)):
		letter = line[1 + index * 4]
		if not_blank(letter):
			stacks[index].append(letter)

def move_crates(stacks, moves):

	for move in moves:
		for i in range(move.count):
			stacks[move.target].append(stacks[move.source].pop())

	return stacks

def split_list(items, split_on):
	for i in range(len(items)):
		if split_on(items[i]):
			return items[:i], items[i+1:]
	assert False
	
def to_instruction(line):
	parts = line.split()
	return Instruction(int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1)

def to_instructions(lines):
	return [to_instruction(line) for line in lines]

def to_stacks(lines):

	stacks = [[] for i in range(1 + len(lines[-1]) // 4)]

	for line in sorted(lines[:-1], reverse = True):
		add_crates(stacks, line)

	return stacks

def top_crates(stacks):
	return [stack[-1] for stack in stacks]

# Main ─────────────────────────────────────────────────────────────────────── #

run_test(DAY, PART, solve)
run_actual(DAY, PART, solve)
