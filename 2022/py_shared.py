#!/usr/bin/env python3

from os.path import exists
from os.path import join
from sys import argv
import traceback

# AOC ──────────────────────────────────────────────────── #

DATA_DIR = "data/"
DATA_FILE = "-data.txt"
TEST_FILE = "-test.txt"
TEST_ANSWERS_FILE = "-test-answers.txt"

def path(day, postfix):
	return join(DATA_DIR, f'{day:02}{postfix}')

def read_data(day):
	return read_lines(path(day, DATA_FILE))

def read_test(day):
	return read_lines(path(day, TEST_FILE))

def read_test_answer(day, index):
	lines = read_lines(path(day, TEST_ANSWERS_FILE))
	return lines[index - 1]

# AOC Main ─────────────────────────────────────────────── #

def run_actual(day, part, solve):
	solve_actual(day, solve)
	nl()

def run_test(day, part, solve):
	nl()
	solve_test(day, part, solve)
	nl()

def solve_actual(day, solve):
	answer = solve(read_data(day))
	print(f"Answer: {answer:<6}")

def solve_test(day, part, solve):
	expected = read_test_answer(day, part)
	actual = str(solve(read_test(day)))

	if actual == expected:
		print(f'Test:   {actual:<6} 👍')
	else:
		print(f'Test:   {actual:<6} (≠ {expected}) ❌')

# Colors ───────────────────────────────────────────────── #

# Special Colors ───────────────────── #

DEFAULT_COLOR='\x1B[0m'
DEFAULT_BACKGROUND='\x1B[49m'
RESET_COLOR='\x1B[0m'

# Foreground ───────────────────────── #

BLACK='\x1B[30m'
DARK_GRAY='\x1B[90m'
LIGHT_GRAY='\x1B[37m'
WHITE='\x1B[97m'
BLUE='\x1B[34m'
CYAN='\x1B[36m'
GREEN='\x1B[32m'
PURPLE='\x1B[35m'
MAGENTA='\x1B[35m'
RED='\x1B[31m'
YELLOW='\x1B[33m'
LIGHT_BLUE='\x1B[94m'
LIGHT_CYAN='\x1B[96m'
LIGHT_GREEN='\x1B[92m'
LIGHT_PURPLE='\x1B[95m'
LIGHT_MAGENTA='\x1B[95m'
LIGHT_RED='\x1B[91m'
LIGHT_YELLOW='\x1B[93m'

# Background ───────────────────────── #

ON_BLACK='\x1B[40m'
ON_DARK_GRAY='\x1B[100m'
ON_LIGHT_GRAY='\x1B[47m'
ON_WHITE='\x1B[107m'
ON_BLUE='\x1B[44m'
ON_CYAN='\x1B[46m'
ON_GREEN='\x1B[42m'
ON_PURPLE='\x1B[45m'
ON_MAGENTA='\x1B[45m'
ON_RED='\x1B[41m'
ON_YELLOW='\x1B[43m'
ON_LIGHT_BLUE='\x1B[104m'
ON_LIGHT_CYAN='\x1B[106m'
ON_LIGHT_GREEN='\x1B[102m'
ON_LIGHT_YELLOW='\x1B[103m'
ON_LIGHT_PURPLE='\x1B[105m'
ON_LIGHT_MAGENTA='\x1B[105m'
ON_LIGHT_RED='\x1B[101m'
ON_LIGHT_YELLOW='\x1B[103m'

# Styles ───────────────────────────── #

BOLD='\x1B[1m'
BLINK='\x1B[5m'
DIMMED='\x1B[2m'
ITALIC='\x1B[3m'
REVERSED='\x1B[7m'
STRIKETHROUGH='\x1B[9m'
UNDERLINE='\x1B[4m'

# User Defined ─────────────────────── #

VAR=f"{ITALIC}{LIGHT_MAGENTA}"


# Arguments ────────────────────────────────────────────── #

def argument(number, default = ''):
	''' Returns the command line parameter
		or the default if it does not exist.

		Index is 0 based.
	'''

	if len(argv) > number + 1:
		return argv[number + 1]
	return default

def arguments():
	return argv[1:]

def argument_count():
	return len(argv) - 1
	
def no_arguments():
	''' Returns True if there are
		no command line parameters
	'''
	return argument_count() == 0

def not_enough_arguments(expected):
	return argument_count() < expected

def outside_argument_range(min, max):
	return argument_count() < min or argument_count() > max

# Utils ────────────────────────────────────────────────── #

def either(value_1, value_2):
	if value_1 is None:
		return value_2
	return value_1

def iif(condition, true_value, false_value=None):
	if condition:
		return true_value
	return false_value

def iif_not(condition, true_value, false_value=None):
	if condition:
		return false_value
	return true_value

# Files ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ #

def file_exists(file_name):
	return exists(file_name)

def read(file_name):
	with open(file_name, 'r') as file:
		return file.read()

def read_lines(file_name):
	with open(file_name, 'r') as file:
		return [line.rstrip('\n') for line in file]

def write(file_name, contents):
	with open(file_name, 'w') as file:
		file.write(contents)

def write_lines(file_name, lines):
	with open(file_name, 'w') as file:
		file.write('\n'.join(lines))


# Strings ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ #

def after(text, match):
	if match in text:
		return text.split(match)[1]
	return text

def after_last(text, match):
	if match in text:
		return text[text.rfind(match) + 1:]
	return text

def before(text, match):
	if match in text:
		return text.split(match)[0]
	return text

def is_blank(value):
	return not value or value.isspace()

def is_empty(value):
	return not value

def not_blank(value):
	return not is_blank(value)

def not_empty(value):
	return not is_empty(value)

def pad(value, length):
	return value.ljust(length)

def to_lines(value):
	return value.split('\n')


# Print ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ #

def nl():
	"""Prints a new line."""
	print("")

