import sys
from random import choice
import socket
import kv_random as rvr
import arguments as args
import servers

k_servers = 1

def send_recv_data_to_server(server, data):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	    s.connect((server.get_ip(), server.get_port()))
	    s.sendall(bytes(data, "ascii"))
	    received_data = s.recv(1024)

	return received_data

def get_data(data_file):
	with open(data_file) as file:
		rows = file.read().split("\n")
	
	return rows

def send_data_to_k_servers(k_servers, row):
	for server in k_servers:
		response = send_recv_data_to_server(server, row)
		print(response)

def send_data_to_servers(servers, data_file, kReplication):
	rows = get_data(data_file)
	for row in rows:
		# k_servers = servers.get_k_random_servers(kReplication)
		send_data_to_k_servers(k_servers, row)


if __name__ == "__main__":
	args = args.get_args(sys.argv[0], sys.argv[1:])

	k_servers =	[servers.Server(args.ip, args.port)]

	servers = servers.get_servers(args.serverFile)

	send_data_to_servers(servers, args.dataToIndex, args.kFactor)