#!/usr/bin/env python
import argparse
import sys
from random import choice
import random_api as rd

def get_args(args=sys.argv[1:]):
	parser = argparse.ArgumentParser(description="Data Creation")

	parser.add_argument("-a", "--ip", help="Server IP", required=True)

	parser.add_argument("-p", "--port", help="Server Port ", required=True)

	return parser.parse_args(args)


if __name__ == "__main__":
	args = get_args(sys.argv[1:])