import parser

class Value:
	def __init__(self, value):
		self.raw_value = value

		if not parser.is_primitive_type(value):
			self.trie = Trie()
			self.build(value)

	def get_raw_value(self):
		return self.raw_value

	def build(self, value):
		pairs = parser.parse_value(value)

		for (key, value) in pairs:
			self.trie.put(key, value)



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
		return self.value.get_raw_value()

	def set_value(self, value):
		self.value = Value(value)

	def get_child_nodes(self):
		return self.child_nodes

	def print_value(self, key, level):
		if self.value:
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

		current_node.set_value(value)

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
			node.set_value(None)

	def print(self):
		self.root_node.print("", 0)
			



if __name__ == '__main__':
	trie = Trie()

	persons = []
	persons.append(('a1', '{ "name" : "Mary" ; "address" : { "street" : "Panepistimiou" ; "number" : 12 } }'))
	persons.append(('b2', '{ "name" : "John" ; "age" : 22 }' ))
	persons.append(('a3', '{ "height" : 1.75 ; "profession" : "student" }'))
	persons.append(('d4e',  "{}"))

	for person in persons:
		trie.put(person[0], person[1])

	trie.print()

	print(trie.get("a1"))
	print(trie.get("b2"))
	print(trie.get("a3"))
	print(trie.get("d4e"))
	print(trie.get("kkk"))
	print("\n\n")

	trie.delete("a1")
	trie.delete("b2")
	trie.delete("a4")

	print(trie.get("a2"))
	print(trie.get("b2"))
	print(trie.get("a3"))
	print(trie.get("d4e"))

