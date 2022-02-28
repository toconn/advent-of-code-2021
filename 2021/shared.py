#!/usr/bin/env python3

COLUMN_1_WIDTH = 30
COLUMN_SEPARATOR = ': '
HEADING_WIDTH = 60
INDENT = '    '

# dot_dot_dot
# heading(heading)
# nl
# print_
# print_2
# print_double
# print_head
# print_heading
# print_indent
# print_is_empty
# print_lines
# print_list
# print_short_heading
# print_title
# print_type
# print2
# short_heading
# title


## General Functions #######################################

def either(value_1, value_2):
    if not value_1:
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

def is_empty(value):
	return not value

def not_empty(value):
	return not is_empty(value)

def pad(value, length):
	return value.ljust(length)

def to_lines(value):
	return value.split('\n')


## File Functions ##########################################

def read_file(file_name):
	with open(file_name, 'r') as file:
		return file.read()

def read_lines(file_name):
	with open(file_name, 'r') as file:
		return [line.rstrip('\n') for line in file]


## Print ###################################################

def dot_dot_dot(text, length):

	if text and len(text) > length:
		return text[:length + 1] + "..."

	return text


def heading(heading):
	print_heading(heading)


def indent(value, value_2, value_3 = None):
	print_indent(value, value_2, value_3)


def nl():
	"""Prints a new line."""
	print("")


def print_(value, value_2 = None):

	if value == None:
		print_("[None]", value_2)
		return

	if value_2 == None:
		print(value)
		return

	try:
		print(value.ljust(COLUMN_1_WIDTH) + COLUMN_SEPARATOR + value_2)
	except TypeError:
		try:
			print(value.ljust(COLUMN_1_WIDTH) + COLUMN_SEPARATOR + str(value_2))
		except TypeError:
			print(value.ljust(COLUMN_1_WIDTH) + COLUMN_SEPARATOR + "[Non Printable Type]")


def print_2(value, value_2 = None):
	print_(value, value_2)


def print_bin (value, value_2):
	if value_2 >=0:
		print_ (value, f"{bin(value_2)[2:]:>8}    {value_2:>3}")
	else:
		print_ (value, f"{'-' + bin(value_2)[3:]:>8}    {value_2:>3}")


def print_double(value, value_2 = None):
	print_(value, value_2)
	nl()


def print_error(value, value_2 = None, show_trace = False):

	if value_2:
		print_ ("Error", value)
		error = value_2
	else:
		print_ ("Error")
		error = value1

	nl()
	print_indent (1, "Type", type(error)) 

	if error.args and error.args[0]:
		print_indent (1, "Message", error.args[0])
	nl()

	if show_trace:
		print(traceback.format_exc())
		nl()


def print_head(heading):
	print_heading(heading)


def print_heading(heading):

	nl()
	print(("** " + heading + "  ").ljust(HEADING_WIDTH, "*"))
	nl()


def print_indent(value, value_2, value_3 = None):

	indent = INDENT * value

	if type (value_3) is str and "\n" in value_3:
		value_3 = "\n\n" + indent + ("\n" + indent).join (value_3.splitlines())

	print_(indent + value_2, value_3)


def print_is_empty(value):

	print_("value", str(value))
	nl()

	# Test Is List

	if type(value) is list:
		print("  is list:    List")
	else:
		print("  is list:    Not List")

	if type(value) == list:
		print("  = list:     List")
	else:
		print("  = list:     Not List")

	nl()

	if value:
		print("  value:      Not Empty")
	else:
		print("  value:      Empty")

	if not value:
		print("  not value:  Empty")
	else:
		print("  not value:  Not Empty")

	nl()

	if value is None:
		print("  is None:    None")
	else:
		print("  is None:    Not None")

	if isinstance(value, list):
		if len(value):
			print("  len:        Not Empty")
		else:
			print("  len:        Empty")

	nl()


def print_lines(value, value_2 = None):
	if value_2:
		print(value + COLUMN_SEPARATOR)
		nl()
		for item in value_2:
			print_indent(1, item)
	else:
		for item in value:
			print(item)
	nl()


def print_list(value, value_2 = None):
	print_lines(value, value_2)


def print_middle(value, value_2 = None):
	nl()
	print_(value, value_2)
	nl()


def print_short_heading(heading):
	nl()
	print(("** " + heading + " **"))
	nl()


def print_title(title):

	nl()
	print("*" * HEADING_WIDTH)
	print(("** " + title + " ").ljust(HEADING_WIDTH - 2) + "**")
	print("*" * HEADING_WIDTH)
	nl()


def print_type(value, value_2 = None):
	if value_2:
		print_(value, type(value_2))
		print_(" ", value_2)
	else:
		print(type(value))
		print(value)


def print_value(value, value_2 = None):
	if value_2:
		print_(value, repr(value_2))
	else:
		print(repr(value))


def print2(value, value_2 = None):
	print_(value, value_2)


def short_heading(heading):
	print_short_heading(heading)


def title(title):
	print_title(title)

