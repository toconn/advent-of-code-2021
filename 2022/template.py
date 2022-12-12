#!/usr/bin/env python3

from py_shared import *
from dataclasses import dataclass

DAY = %day%
PART = %part%;

# Types ────────────────────────────────────────────────────────────────────── #

@dataclass
class xxx:
	pass

# Solution ─────────────────────────────────────────────────────────────────── #

def solve(lines):
	return sum([solve_line(line) for line in lines])

def solve_line(line):
	return 0

# Main ─────────────────────────────────────────────────────────────────────── #

run_test(DAY, PART, solve)
# run_actual(DAY, PART, solve)
