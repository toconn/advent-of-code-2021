#!/usr/bin/env python3

from shared import *
from dataclasses import dataclass

from day_01_data import *

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


def top_three_calories(calories_by_elf):

	top_calories = [0, 0, 0]
	
	for calories in calories_by_elf:
		if calories > top_calories[2]:
			top_calories[2] = calories
			top_calories.sort(reverse = True)

	return top_calories


elf_inventory = to_calories_by_elf(DATA_1)
top_calories = top_three_calories(elf_inventory)
total = sum(top_calories)

nl()
print("Sum of Top Calories", total)
