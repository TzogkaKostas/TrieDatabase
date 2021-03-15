#!/usr/bin/env python3
# GNU All-Permissive License
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.

import argparse
import sys

def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Data Creation")
    parser.add_argument("-n", "--nlines", help="Number of lines", required=True)
    parser.add_argument("-d", "--depth", help="Maximum level of nesting")
    parser.add_argument("-m", "--number", type=int, help="Maximum number of keys inside each value")
    parser.add_argument("-l", "--verbose",dest='verbose',action='store_true', help="Verbose mode.")
    options = parser.parse_args(args)
    return options

options = getOptions(sys.argv[1:])

if options.verbose:
    print("Verbose mode on")
else:
    print("Verbose mode off")

print(options.input)
print(options.output)
print(options.number)