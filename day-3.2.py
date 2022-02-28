#!/usr/bin/env python3

from data import *
from shared import *


# data = DAY_3_TEST.splitlines()
data = DAY_3_ACTUAL.splitlines()


# Bit Tools #########

def bit_length(data):
	return len(data[0])

def count_ones(data, position):
	count = 0
	for item in data:
		if item[position] == '1':
			count += 1
	return count

def has_bit(item, position, value):
	return item[position] == value

def greatest_bit(data, one_count):
	return '0' if one_count < (len(data) / 2) else '1'

def least_bit(data, one_count):
	return '1' if one_count < (len(data) / 2) else '0'

def to_int(binary):
	return int(binary, 2)


# System Calc

def calc_epsilon(data):
	value = ''
	for i in range(bit_length(data)):
		value += least_bit(data, count_ones(data, i))
	return to_int(value)

def calc_gamma(data):
	value = ''
	for i in range(bit_length(data)):
		value += greatest_bit(data, count_ones(data, i))
	return to_int(value)

def calc_oxygen(data, position = 0):
	
	if len(data) == 1:
		return to_int(data[0])
	
	bit = greatest_bit(data, count_ones(data, position))

	return calc_oxygen(
				[item for item in data if has_bit(item, position, bit)],
				position + 1)

def calc_co2(data, position = 0):
	
	if len(data) == 1:
		return to_int(data[0])
	
	bit = least_bit(data, count_ones(data, position))

	return calc_co2(
				[item for item in data if has_bit(item, position, bit)],
				position + 1)



# gamma = calc_gamma(data)
# epsilon = calc_epsilon(data)
# print (gamma, epsilon, gamma * epsilon)

oxygen = calc_oxygen(data)
co2 = calc_co2(data)
print (oxygen, co2, oxygen * co2)

