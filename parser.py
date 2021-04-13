import json

def is_primitive_type(value):
	if value == None:
		return True

	if not "{" in value and not "}" in value and not ":" in value:
		return True

	return False

def simpleKV_to_JSON(data):
	data = data.replace(" ", "")
	data = data.replace(";", ",")
	try:
		res = json.loads(data)
		return res
	except json.decoder.JSONDecodeError:
		return -1

def JSON_to_simpleKV(data):
	data = str(data)
	data = data.replace(",", ";")
	data = data.replace("\'", "\"")

	return data

def parse_value(value):
	value_as_json = simpleKV_to_JSON(value)
	if value_as_json == -1:
		return -1

	pairs = []
	for key in value_as_json:
		value = JSON_to_simpleKV(value_as_json[key])

		pairs.append((key, value))

	return pairs