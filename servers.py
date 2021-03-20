from random import sample

class Server:
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port

	def get_ip(self):
		return self.ip

	def get_port(self):
		return self.port

class Servers:
	def __init__(self):
		self.servers = []

	def add_server(self, server):
		self.servers.append(server)

	def get_k_random_servers(self, k):
		return sample(self.servers, k)

	def print_servers(self):
		for server in self.servers:
			print(server.get_ip(), server.get_port())

def get_servers(server_file):
	with open(server_file) as file:
		rows = file.read().split("\n")

	servers = Servers()
	for row in rows:
		ip, port = row.split(" ")[0], int(row.split(" ")[1])
		servers.add_server(Server(ip, port))

	return servers