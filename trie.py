class Value:
	def __init__(self, value_as_string):
		self.value_as_string = value_as_string

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

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value

	def get_child_nodes(self):
		return self.child_nodes

	def print_value(self, key):
		if self.value:
			print(key, ":", self.value)

	def print(self, key):
		for char in self.get_child_nodes():
			# print("#", key, "#")
			self.get_child_node(char).print_value(key + char)
			self.get_child_node(char).print(key + char)



class Trie:
	def __init__(self):
		self.root_node = TrieNode()

	def insert(self, key, value):
		current_node = self.root_node

		for char in key:
			if not current_node.has_child_node(char):
				current_node = current_node.set_child_node(char)

		current_node.set_value(value)

	def print(self):
		self.root_node.print("")
			



if __name__ == '__main__':
	trie = Trie()

	persons = []
	persons.append(('a1', '{ "name" : "John" ; "age" : 22 }' ))
	persons.append(('b2', '{ "name" : "Mary" ; "address" : { "street" : "Panepistimiou" ; "number" : 12 } }'))
	persons.append(('a3', '{ "height" : 1.75 ; "profession" : "student" }'))
	persons.append(('d4',  "{}"))

	for person in persons:
		trie.insert(person[0], person[1])

	trie.print()