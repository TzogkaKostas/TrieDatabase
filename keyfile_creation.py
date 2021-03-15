import argparse
import sys

import random_api as rd

def getOptions(args=sys.argv[1:]):
	parser = argparse.ArgumentParser(description="Data Creation")

	parser.add_argument("-n", "--nlines", type=int, default=10,
		help="indicates the number of lines (i.e. separate data) that we would "
		"like to generate (e.g. 1000).")

	parser.add_argument("-k", "--keyfile", help=" is a file containing a "
		"space-separated list of key names and their data types that we "
		"can potentially use for creating data. For example: name string\n"
		"age int\nheight float\nstreet string\nlevel int ...", required=True)

	return parser.parse_args(args)

def get_random_lines(nlines):
	lines = ""
	for i in range(nlines):
		lines += rd.get_random_key_name() + " " + rd.get_random_type()
		if i != nlines - 1:
			lines += "\n"

	return lines

if __name__ == "__main__":
	options = getOptions(sys.argv[1:])

	data = get_random_lines(options.nlines)

	print(data)

	with open(options.keyfile, "w") as file:
		file.write(data)