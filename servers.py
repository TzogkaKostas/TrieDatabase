from random import sample
from kvBroker import is_server_up

class Server:
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port

	def get_ip(self):
		return self.ip

	def get_port(self):
		return self.port

	def to_string(self):
		return self.ip, self.port

class Servers:
	def __init__(self):
		self.servers = []

	def add_server(self, server):
		self.servers.append(server)

	def get_k_random_servers(self, k):
		return sample(self.servers, k)

	def get_up_servers(self):
		k_random_up_servers = []
		for server in self.servers:
			if is_server_up(server.get_ip(), server.get_port()) == True:
				k_random_up_servers.append(
						Server(server.get_ip(), server.get_port()))
		
		return k_random_up_servers

	def get_k_random_up_servers(self, k):
		k_random_up_servers = []
		num_of_up_servers = 0
		for server in sample(self.servers, len(self.servers)):
			if is_server_up(server.get_ip(), server.get_port()) == True:
				k_random_up_servers.append(
						Server(server.get_ip(), server.get_port()))
				num_of_up_servers += 1

			if num_of_up_servers >= k:
				return k_random_up_servers
		
		return []		

	def get_servers(self):
		return self.servers

	def get_total(self):
		return len(self.servers)

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