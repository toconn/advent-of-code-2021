#!/usr/bin/env python3

from py_shared import *
from dataclasses import dataclass

from py_01_data import *

# Solution ─────────────────────────────────────────────────────────────────── #

def to_calories_by_elf(data):

	by_elf = []
	calories = 0

	for value in data.splitlines():
		if is_blank(value):
			by_elf.append(calories)
			calories = 0
		else:
			calories += int(value)

	by_elf.append(calories)

	return by_elf


calories_by_elf = to_calories_by_elf(DATA_1)
max_calories = max(calories_by_elf)

nl()
print("Max Calories", max_calories)
