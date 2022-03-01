#!/usr/bin/env python3

from day_2_data import *
from shared import *
from dataclasses import dataclass
from collections import Counter


@dataclass
class Password:
	letter : str
	min: int
	max: int
	password: str

def parse(data):
	return [to_password(item) for item in data.splitlines()]

def to_password(line):

	range, letter, password = line.split()
	min, max = range.split('-')

	return Password(
		letter[0],
		int(min),
		int(max),
		password)

# Part 1 ######################

def count_valid_by_count(passwords):
	return len([password for password in passwords if is_valid_by_count(password)])

def is_valid_by_count(password):
	counter = Counter(password.password)
	count = counter[password.letter]
	return count >= password.min and count <= password.max


print('1.1 count:', count_valid_by_count(data))


# Part 2 ######################

def count_valid_by_position(passwords):
	return len([password for password in passwords if is_valid_by_position(password)])

def is_valid_by_position(password):
	return ((password.password[password.min - 1] == password.letter and password.password[password.max - 1] != password.letter) 
		or (password.password[password.min - 1] != password.letter and password.password[password.max - 1] == password.letter))


data = parse(DATA_TEST)
data = parse(DATA_ACTUAL)


nl()
for item in data:
	print(item, is_valid_by_position(item))
nl()
print('1.2 count:', count_valid_by_position(data))


