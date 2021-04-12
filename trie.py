import parser

class Value:
	def __init__(self, value):
		self.raw_value = value
		self.trie = None

		if not parser.is_primitive_type(value):
			self.trie = Trie()
			self.build(value)

	def get_raw_value(self):
		return self.raw_value

	def build(self, value):
		pairs = parser.parse_value(value)

		for (key, value) in pairs:
			self.trie.put(key, value)

	def find(self, key):
		if not self.trie:
			return None
		
		return self.trie._get_node(key)

	def print(self):
		if self.trie:
			self.trie.print()
		else:
			print("#", self.raw_value, "#")


class TrieNode:
	def __init__(self):
		self.child_nodes = dict()
		self.value = None

	def get_child_node(self, char):
		return self.child_nodes[char]

	def set_child_node(self, char):
		new_trie_node = TrieNode()
		self.child_nodes[char] = new_trie_node

		return new_trie_node

	def has_child_node(self, char):
		if char in self.child_nodes:
			return True
		
		return False

	def get_raw_value(self):
		if not self.value:
			return None

		return self.value.get_raw_value()

	def get_value(self):
		return self.value

	def set_raw_value(self, value):
		self.value = Value(value)

	def set_value(self, value):
		self.value = value

	def get_child_nodes(self):
		return self.child_nodes

	def print_value(self, key, level):
		if self.value and self.get_raw_value():
			print(level*'\t' + key +  " : " + self.get_raw_value())

	def print(self, key, level):
		for char in self.get_child_nodes():
			self.get_child_node(char).print_value(key + char, level)
			self.get_child_node(char).print(key + char, level + 1)



class Trie:
	def __init__(self):
		self.root_node = TrieNode()

	def put(self, key, value):
		current_node = self.root_node

		for char in key:
			if not current_node.has_child_node(char):
				current_node.set_child_node(char)
			current_node = current_node.get_child_node(char)

		current_node.set_raw_value(value)

	def _get_node(self, key):
		current_node = self.root_node

		for char in key:
			if current_node.has_child_node(char):
				current_node = current_node.get_child_node(char)
			else:
				return None

		return current_node

	def get(self, key):
		node = self._get_node(key)
		if node:
			return node.get_raw_value()

		return None

	def delete(self, key):
		node = self._get_node(key)
		if node:
			value = node.get_value()
			if value:
				node.set_value(None)
				return value
		
		return None

	def query(self, key_path):
		keys = key_path.split(".")
		current_node = self._get_node(keys[0])
		if not current_node:
			return None

		for key in keys[1:]:
			current_node = current_node.get_value().find(key)
			if not current_node:
				return None
			
		return current_node.get_raw_value()	

	def print(self):
		self.root_node.print("", 0)		