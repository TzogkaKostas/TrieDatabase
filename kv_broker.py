#!/usr/bin/env python
import argparse
import sys
from random import choice
import random_api as rd

def get_args(args=sys.argv[1:]):
	parser = argparse.ArgumentParser(description="Data Creation")

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


class KV_Store:
	def __init__(self, key, value):
		self.key = key
		self.value = value

if __name__ == "__main__":
	args = get_args(sys.argv[1:])