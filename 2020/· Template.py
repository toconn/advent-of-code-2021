#!/usr/bin/env python3

from day_x_data import *
from shared import *
from dataclasses import dataclass


def parse(data):
	return data.splitlines()


data = parse(DATA_TEST)
# data = parse(DATA_ACTUAL)