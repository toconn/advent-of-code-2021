#!/usr/bin/env python3

from data import *
from shared import *
from dataclasses import dataclass

# data = DAY_2_TEST
data = DAY_2_ACTUAL

@dataclass
class Command:
	name: str
	value: int

@dataclass
class Position:
	distance: int = 0
	depth: int = 0

	def value(self):
		return self.distance * self.depth

def forward(position, value):
	return Position(position.distance + value, position.depth)

def up(position, value):
	return Position(position.distance, position.depth - value)

def down(position, value):
	return Position(position.distance, position.depth + value)

def update(position, command):
	return COMMAND_DICT[command.name](position, command.value)

def to_command(text):
	name, value = text.split()
	return Command(name.lower(), int(value))

COMMAND_DICT = {
	'forward': forward,
	'up': up,
	'down': down}

commands = [to_command(line) for line in data.splitlines()]

position = Position()
for command in commands:
	position = update(position, command)

print (position.value(), position.distance, position.depth)
