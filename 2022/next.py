#!/usr/bin/env python3

from os import listdir
from os.path import join
from fnmatch import filter
from sys import exit
from subprocess import run

from py_shared import *


HELP = f'''Usage: next  next | day
'''

ALREADY_EXISTS = '''Matching files already exist.
'''

PYTHON_FILE = 'py_%day%_%part%.py'
PYTHON_TEMPLATE = 'template.py'
RUSH_FILE = 'rust_%day%_%part%.rs'
RUST_TEMPLATE = 'template.rs'

DATA_DIR = 'data'
DATA_FILE = '%day%-data.txt'
TEST_FILE = '%day%-test.txt'
TEST_ANSWER_FILE = '%day%-test-answers.txt'

PROG_FILE_SEARCH = 'py_*_1.py'

DATA_CONTENTS = '''
'''

ANSWER_CONTENTS = '''0
0'''


def arguments_not_valid():

	if argument_count() != 1:
		return True

	argument_1 = argument(0).lower()
	return not (argument_1 == 'next' or argument_1 == 'n' or argument_1.isdigit())

def create_files(day):

	if file_exists(path_actual(PYTHON_FILE, day, 1)) or file_exists(data_file_path(DATA_FILE, day)):
		show_already_exists()
		exit()

	create_python_files(day)
	create_rust_files(day)
	create_data_files(day)

def create_data_file(path, content):
	print(f'Creating {path}...')
	write(path, content)

def create_data_files(day):
	create_data_file(data_file_path(DATA_FILE, day), DATA_CONTENTS)
	create_data_file(data_file_path(TEST_FILE, day), DATA_CONTENTS)
	create_data_file(data_file_path(TEST_ANSWER_FILE, day), ANSWER_CONTENTS)

def create_python_files(day):
	create_program_files(read(PYTHON_TEMPLATE), PYTHON_FILE, day)

def create_rust_files(day):
	create_program_files(read(RUST_TEMPLATE), RUSH_FILE, day)

def create_program_file(path, content):
	print (f'Creating {path}...')
	write(path, content)
	make_executable(path)

def create_program_files(content, file_name, day):
	create_program_file(path_actual(file_name, day, 1), update(content, day, 1))
	create_program_file(path_actual(file_name, day, 2), update(content, day, 2))

def data_file_path(name, day):
	return join(DATA_DIR, path_actual(name, day))

def make_executable(file):
	run(f'chmod +x {file}', shell=True)

def next_day():
	argument_1 = argument(0).lower()

	if argument_1.isdigit():
		return int(argument_1)

	return next_day_file()

def next_day_file():
	return max(read_file_numbers()) + 1

def path_actual(content, day, part = 1):
	return content.replace('%day%', f'{day:02}').replace('%part%', f'{part}')

def read_file_names():
	return filter(listdir('.'), PROG_FILE_SEARCH)

def read_file_numbers():
	return [int(file.split('_')[1]) for file in read_file_names()]

def show_already_exists():
	print(ALREADY_EXISTS)

def show_help():
	print(HELP)

def update(content, day, part):
	return content.replace('%day%', f'{day}').replace('%part%', f'{part}')

# Main ─────────────────────────────────────────────────── #

nl()

if arguments_not_valid():
	show_help()
	exit()

print ("creating files:")
nl()
create_files(next_day())

