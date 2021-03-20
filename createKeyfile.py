import sys

import kv_random as ra
import arguments as args

def get_random_lines(nlines):
	lines = ""
	for i in range(nlines):
		lines += ra.get_random_key_name() + " " + ra.get_random_type()
		if i != nlines - 1:
			lines += "\n"

	return lines

if __name__ == "__main__":
	options = args.get_args(sys.argv[0], sys.argv[1:])

	data = get_random_lines(options.nlines)

	print(data)

	with open(options.keyfile, "w") as file:
		file.write(data)