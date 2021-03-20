from random import randint, uniform, choice, choices
from string import digits, ascii_lowercase, ascii_uppercase

def get_random_key_name():
	return get_random_string()

def get_random_type():
	datatypes = ["string", "int", "float", "KV"]
	return choice(datatypes)

def get_random_string(length=5):
	return ''.join(choices(ascii_uppercase + digits + ascii_lowercase, 
			k=length))

def get_random_int(start=0, end=10):
	return randint(start, end)

def get_random_float(start=0, end=10):
	return float("{:.2f}".format(uniform(start, end)))