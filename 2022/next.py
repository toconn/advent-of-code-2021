#!/usr/bin/env python3

from os import listdir
from fnmatch import filter
from shared import *
from sys import exit


HELP = f'''{YELLOW}Usage: next  next | {VAR}day{RESET_COLOR}
'''

ALREADY_EXISTS = '''Matching files already exist.
'''

PROG_TEMPLATE = '· template day.py'
DATA_TEMPLATE = '· template day_data.py'
DATA_IMPORT_REPLACE = 'day_data'

PROG_FILE = 'day_{:02}_{}.py'
DATA_IMPORT = 'day_{:02}_data'
PROG_FILE_SEARCH = 'day_*_1.py'


def arguments_not_valid():
	if argument_count() != 1:
		return True

	argument_1 = argument(0).lower()
	return not (argument_1 == 'next' or argument_1 == 'n' or argument_1.isdigit())

def create_files(day):
	if file_exists(prog_file_name(day, 1),) or file_exists(data_file_name(day)):
		show_already_exists()
		exit()
	create_prog_file(day)
	create_data_file(day)

def create_data_file(day):
	content = read(DATA_TEMPLATE)
	write(data_file_name(day), content)

def create_prog_file(day):
	content = read(PROG_TEMPLATE)
	actual = content.replace(DATA_IMPORT_REPLACE, data_import(day))
	write(prog_file_name(day, 1), actual)
	write(prog_file_name(day, 2), actual)

def data_import(day):
	return DATA_IMPORT.format(day)

def data_file_name(day):
	return data_import(day) + '.py'

def prog_file_name(day, number):
	return PROG_FILE.format(day, number)

def next_day():
	argument_1 = argument(0).lower()

	if argument_1.isdigit():
		return int(argument_1)

	return next_day_file()

def next_day_file():
	return max(read_file_numbers()) + 1

def read_file_names():
	return filter(listdir('.'), PROG_FILE_SEARCH)

def read_file_numbers():
	return [int(file.split('_')[1]) for file in read_file_names()]

def show_already_exists():
	print(ALREADY_EXISTS)

def show_help():
	print(HELP)

# Main ─────────────────────────────────────────────────── #

nl()

if arguments_not_valid():
	show_help()
	exit()

create_files(next_day())

