#!/usr/bin/env python3

from shared import *
from dataclasses import dataclass


# data = DAY_1_TEST.splitlines()
data = DAY_1_ACTUAL.splitlines()


def calc_epsilon(data):
	value = ''
	for count in count_occurences(data):
		value += '1' if count < (len(data) / 2) else '0'
	return to_int(value)

def calc_gamma(data):
	value = ''
	for count in count_occurences(data):
		value += '1' if count > (len(data) / 2) else '0'
	return to_int(value)

def count_occurences(data):
	counts = [0] * len(data[0])
	for item in data:
		for i in range(len(data[0])):
			if item[i] == '1':
				counts[i] = counts[i] + 1
	return counts

def to_int(binary):
	return int(binary, 2)

gamma = calc_gamma(data)
epsilon = calc_epsilon(data)

print (gamma, epsilon, gamma * epsilon)
