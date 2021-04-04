import json

def is_primitive_type(value):
	# return True

	if value == None:
		return True

	if not "{" in value:
		return True

	return False

def simpleKV_to_JSON(data):
	data = data.replace(" ", "")
	data = data.replace(";", ",")
	return json.loads(data)

def JSON_to_simpleKV(data):
	data = str(data)
	data = data.replace(",", ";")
	data = data.replace("\'", "\"")

	# if type(value) != str:
	# 	value = str(value)
	# else:
	# 	value = "\"" + value + "\""

	return data

def parse_value(value):
	value_as_json = simpleKV_to_JSON(value)

	pairs = []
	for key in value_as_json:
		value = value_as_json[key]
		value = JSON_to_simpleKV(value)

		key = "\"" + key + "\""

		pairs.append((key, value))

	return pairs



# if __name__ == '__main__':
# 	value = '{ "name" : 1 ; "name2" : "george" ; "name3" :  { "street" : "Panepistimiou"}  }'

# 	pairs = parse_value(value)

# 	print(pairs)