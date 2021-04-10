import sys
import os
from random import choice
import socket
import kv_random as rvr
import arguments as args
import servers
import readline

MAX_MESSAGE_SIZE = 1024*1000

k_servers = 1 # TODO: REMOVE THIS

def string_to_bytes(data):
	return bytes(data, "ascii")

def bytes_to_string(data):
	return data.decode()

def send_recv_data_to_server(server, data):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((server.get_ip(), server.get_port()))
		s.sendall(string_to_bytes(data))
		received_data = s.recv(MAX_MESSAGE_SIZE)

	return received_data

def get_data(data_file):
	with open(data_file) as file:
		rows = file.read().split("\n")
	
	return rows

def is_valid(response):
	if response == b"OK":
		return True
	else:
		return False

def send_data_to_k_servers(k_servers, data):
	for server in k_servers:
		print(server.to_string(), "<--", data)
		response = send_recv_data_to_server(server, data)
		print(bytes_to_string(response))

def index_data_to_servers(servers, data_file, kReplication):
	rows = get_data(data_file)
	for row in rows:
		if row:
			k_servers = servers.get_k_random_servers(kReplication) # TODO: UNCOMMENT THIS
			send_data_to_k_servers(k_servers, "PUT " + row)

def is_server_up(ip, port):
	response = True
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect((ip, port))
	except:
		response = False
	finally:
		sock.close()
		return response

def are_k_server_down(servers, k):
	num_of_down_servers = 0
	for server in servers:
		if is_server_up(server.get_ip(), server.get_port()) == False:
			num_of_down_servers += 1

		if num_of_down_servers >= k:
			return True
	
	return False

def handle_GET_or_QUERY_command(command, servers, kReplication):
	if are_k_server_down(servers.get_servers(), kReplication) == True:
		print(kReplication, "or more servers are down and therefore the correct"
		" output cannot be guaranteed.")
		return
	
	k_servers = servers.get_k_random_servers(kReplication) # TODO: UNCOMMENT THIS
	send_data_to_k_servers(k_servers, command)

def handle_DELETE_command(command, servers):
	if are_k_server_down(servers.get_servers(), 1) == True:
		print("At least 1 server is down. DELETE cannot be reliably executed.")
		return

	send_data_to_k_servers(servers.get_servers(), command) # TODO: REPLACE k_servers with servers (ALL)

def handle_user_input(user_input, servers, kReplication):
	command_name = user_input.split(" ")[0]
	if command_name == "GET" or  command_name == "QUERY":
		handle_GET_or_QUERY_command(user_input, servers, kReplication)
	elif command_name == "DELETE":
		handle_DELETE_command(user_input, servers)
	elif command_name == "clear":
		os.system("clear")
	else:
		print("unkown command...")

def handle_user_inputs(servers, kReplication):
	while True:
		user_input = input("KVcmd>")
		handle_user_input(user_input, servers, kReplication)


if __name__ == "__main__":
	args = args.get_args(sys.argv[0], sys.argv[1:])

	# k_servers = [servers.Server(args.ip, args.port)] # TODO: REMOVE THIS

	servers = servers.get_servers(args.serverFile) 

	# index_data_to_servers(servers, args.dataToIndex, args.kFactor)

	handle_user_inputs(servers, args.kFactor) # TODO: CHANGE k_server to servers