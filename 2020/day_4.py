#!/usr/bin/env python3

from day_4_data import *
from shared import *
from dataclasses import dataclass
from re import findall
from re import match
from re import search
from re import split


def parse(data):
	return [item for item in data.split('\n\n')]

def product(items):
	value = 1
	for item in items:
		value *= item
	return value




# Data ########################

data = parse(DATA_TEST)
data = parse(DATA_ACTUAL)


fields = {
		'byr': 'Birth Year',
		'iyr': 'Issue Year',
		'eyr': 'Expiration Year',
		'hgt': 'Height',
		'hcl': 'Hair Color',
		'ecl': 'Eye Color',
		'pid': 'Passport ID',
		'cid': 'Country ID'}

required = {
		'byr',
		'iyr',
		'eyr',
		'hgt',
		'hcl',
		'ecl',
		'pid'}


# Part 1 ######################

def is_valid(passport):
	return len(required & passport) == len(required)

def count_valid(passports):
	return ([is_valid(passport) for passport in passports]).count(True)

def to_fields(data):
	return set(findall(r'[a-zA-Z]{3}(?=\:)', data))

def to_passports(data):
	return [to_fields(item) for item in data]

passports = to_passports(data)

print ('Total:', len(passports))
print ('Valid:', count_valid(passports))



# Part 2 ######################

def get_digits(value):
	return search(r'\d+', value).group()

def to_passports_with_data(data):
	return [to_passport_with_data(item) for item in data]

def to_passport_with_data(data):
	passport = {}
	fields = split(r'\s+', data)
	for field in fields:
		name, value = field.split(':')
		passport[name] = value
	return passport

def between(value, min, max):
	return int(value) >= min and int(value) <= max

def is_birth_year(value):
	return between(value, 1920, 2002)

def is_expiration_year(value):
	return between(value, 2020, 2030)

def is_issue_year(value):
	return between(value, 2010, 2020)

def is_height(value):
	if value.endswith('cm'):
		return between(get_digits(value), 150, 193)
	
	if value.endswith('in'):
		return between(get_digits(value), 59, 76)
	
	return False

def is_hair_color(value):
	return match(r'#[0-9a-f]{6}$', value) is not None

def is_eye_color(value):
	return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def is_passport_id(value):
	return match(r'\d{9}$', value) is not None


field_validation = {
		'byr': is_birth_year,
		'iyr': is_issue_year,
		'eyr': is_expiration_year,
		'hgt': is_height,
		'hcl': is_hair_color,
		'ecl': is_eye_color,
		'pid': is_passport_id,
}

def is_valid_field(name, value):

	if name not in field_validation:
		print(name, value, True , '+')
		return True

	print(name, value, field_validation[name](value))
	return field_validation[name](value)

def is_valid_2(passport):

	if len(required & set(passport.keys())) != len(required):
		return False

	checks = [is_valid_field(name, value) for name, value in passport.items()]

	return checks.count(False) == 0

def count_valid_2(passports):
	return ([is_valid_2(passport) for passport in passports]).count(True)


passports = to_passports_with_data(data)

print ('Valid:', count_valid_2(passports))




