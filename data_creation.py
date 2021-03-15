#!/usr/bin/env python
import argparse
import sys
from random import choice
import random_api as rd

def get_args(args=sys.argv[1:]):
	parser = argparse.ArgumentParser(description="Data Creation")

	parser.add_argument("-n", "--nlines", type=int, default=5,
		help="indicates the number of lines (i.e. separate data) that we would "
		"like to generate (e.g. 1000).")

	parser.add_argument("-d", "--depth", type=int, default=2,
		help="is the maximum level of nesting "
		"(i.e. how many times in a line a value can have a set of key :"
		"values). Zero means no nesting, i.e. there is only one set of "
		"key-values per line (in the value of the high level key).")

	parser.add_argument("-m", "--mkeys", type=int, default=3,
		help="is the maximum number of keys inside each value.")

	parser.add_argument("-l", "--length", type=int, default=4,
		help="is the maximum length of a  "
		"string value whenever you need to generate a string. For example 4 "
		"means that we can generate Strings of up to length 4 (e.g. 'ab', "
		"'abcd', 'a'). We should not generate empty strings (i.e. '' is not"
		"correct). Strings can be only letters (upper and lowercase) and "
		"numbers. No symbols.")

	parser.add_argument("-k", "--keyfile", help=" is a file containing a "
		"space-separated list of key names and their data types that we "
		"can potentially use for creating data. For example: name string\n"
		"age int\nheight float\nstreet string\nlevel int ...", required=True)

	return parser.parse_args(args)


def get_random_value(args, keys, data_type, depth):
	if data_type == "int":
		return str(rd.get_random_int())
	elif data_type == "float":
		return str(rd.get_random_float())
	elif data_type == "string":
		return rd.get_random_string(args.length)
	elif data_type == "KV":
		return get_random_pairs(args, keys, depth - 1)

def get_random_key(keys, depth):
	(key, data_type) = choice(keys)
	while depth == 0 and data_type == "KV":
		(key, data_type) = choice(keys)

	return (key, data_type)

def get_random_pair(args, keys, depth):
	(key, data_type) = get_random_key(keys, depth)
	return "\"" + key + "\" : " + get_random_value(args, keys, data_type, depth)

def read_keys_from_file(keyfile):
	with open(keyfile, "r") as file:
		lines = file.read().split("\n")
	
	keys = []
	for line in lines:
		keys.append((line.split(' ')[0], line.split(' ')[1]))

	return keys

def select_num_of_keys(mkeys):
	return choice(range(0, mkeys + 1))


def get_random_pairs(args, keys, depth):
	values = "{"
	num_of_keys = select_num_of_keys(args.mkeys)

	for i in range(num_of_keys):
		values += get_random_pair(args, keys, depth)
		if i != num_of_keys - 1:
			values += " ; "

	return values + "}"

def get_top_key(i):
	return "\"key_" + str(i) + "\""

def get_random_lines(args):
	keys = read_keys_from_file(args.keyfile)

	lines = ""
	for i in range(args.nlines):
		lines += get_top_key(i) + " : " + get_random_pairs(args, keys, args.depth) + "\n"
	
	return lines


if __name__ == "__main__":
	args = get_args(sys.argv[1:])

	data = get_random_lines(args)

	print(data)