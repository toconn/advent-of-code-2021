#!/usr/bin/env python3

from data import *
from shared import *

title("Day 1 - Count Raises")

# data = DAY_1_TEST
data = DAY_1_ACTUAL


last = data[0]
count = 0
for item in data[1:]:
	if item > last:
		count += 1
	last = item

print (count)

