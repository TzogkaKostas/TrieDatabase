import sys
from random import choice
import kv_random as kvr
import arguments as args

chosen_keys = []

def get_random_value(args, keys, data_type, depth):
	if data_type == "int":
		return str(kvr.get_random_int())
	elif data_type == "float":
		return str(kvr.get_random_float())
	elif data_type == "string":
		return "\"" + kvr.get_random_string(args.length) + "\""
	elif data_type == "KV":
		return get_random_pairs(args, keys, depth - 1)


def get_available_keys(keys, depth):
	if depth == 0:
		return [(key, data_type) for (key, data_type) in keys if data_type != "KV"]

	return keys


def get_random_key(keys, depth):
	available_keys = get_available_keys(keys, depth)
	if available_keys == []:
		return (None, None)

	(key, data_type) = choice(available_keys)

	keys.remove((key, data_type))

	return (key, data_type)

def get_random_pair(args, keys, depth):
	(key, data_type) = get_random_key(keys, depth)

	if key == None:
		return ""

	return "\"" + key + "\" : " + get_random_value(args, keys, data_type, depth)

def read_keys_from_file(keyfile):
	with open(keyfile, "r") as file:
		lines = file.read().split("\n")
	
	keys = []
	for line in lines:
		keys.append((line.split(' ')[0], line.split(' ')[1]))

	return keys

def select_random_num_of_keys(mkeys):
	return choice(range(0, mkeys + 1))

def get_random_pairs(args, keys, depth):
	pairs = "{"
	num_of_keys = select_random_num_of_keys(args.mkeys)

	if num_of_keys > 0:
		pairs += get_random_pair(args, keys, depth)

	for i in range(num_of_keys - 1):
		pair = get_random_pair(args, keys, depth)

		if pair != "":
			pairs +=  " ; " + pair

	return pairs + "}"

def get_top_key(i):
	return "\"key_" + str(i) + "\""

def get_random_lines(args):
	keys = read_keys_from_file(args.keyfile)

	lines = ""
	for i in range(args.nlines):
		chosen_keys = []
		lines += get_top_key(i) + " : " + \
			get_random_pairs(args, keys, args.depth)

		if i != args.nlines - 1:
			lines += "\n"

	return lines


if __name__ == "__main__":
	args = args.get_args(sys.argv[0], sys.argv[1:])

	data = get_random_lines(args)

	print(data)