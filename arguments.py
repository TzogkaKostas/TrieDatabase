import argparse
import sys

def get_args(source_name, args):
	if source_name == "createKeyfile.py":
		return get_args1(args)
	elif source_name == "createData.py":
		return get_args2(args)
	elif source_name == "kvBroker.py":
		return get_args3(args)
	elif source_name == "kvServer.py":
		return get_args4(args)



def get_args1(args):
	parser = argparse.ArgumentParser(description="KeyFile Creation")

	parser.add_argument("-n", "--nlines", type=int, default=10,
		help="indicates the number of lines (i.e. separate data) that we would "
		"like to generate (e.g. 1000).")

	parser.add_argument("-k", "--keyfile", help=" is a file containing a "
		"space-separated list of key names and their data types that we "
		"can potentially use for creating data. For example: name string\n"
		"age int\nheight float\nstreet string\nlevel int ...", required=True)

	return parser.parse_args(args)


def get_args2(args):
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

def get_args3(args):
	parser = argparse.ArgumentParser(description="KV Broker")

	parser.add_argument("-s", "--serverFile",
		help="is a space separated list of server IPs and their respective "
		"ports that will be listening for queries and indexing commands.",
		required=True)

	parser.add_argument("-i", "--dataToIndex",
		help="is a file containing data that was output from the previous "
		"part of the project that was generating the data.", required=True)

	parser.add_argument("-k", "--kFactor", type=int, default=2,
		help="is the replication factor, i.e. how many different servers will "
		"have the same replicated data.")

	return parser.parse_args(args)

def get_args4(args):
	parser = argparse.ArgumentParser(description="KV Server")

	parser.add_argument("-a", "--ip", help="Server IP", required=True)

	parser.add_argument("-p", "--port", help="Server Port ", type=int,
		required=True)

	return parser.parse_args(args)