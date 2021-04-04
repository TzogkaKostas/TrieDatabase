import sys
from random import choice
import socket
import kv_random as rvr
import arguments as args
import servers

k_servers = 1 # TODO: REMOVE THIS

def string_to_bytes(data):
	return bytes(data, "ascii")

def send_recv_data_to_server(server, data):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((server.get_ip(), server.get_port()))
		s.sendall(string_to_bytes(data))
		received_data = s.recv(1024)

	return received_data

def get_data(data_file):
	with open(data_file) as file:
		rows = file.read().split("\n")
	
	return rows

def is_valid(response):
	if response == "OK":
		return True
	else:
		return False

def send_data_to_k_servers(k_servers, data):
	for server in k_servers:
		response = send_recv_data_to_server(server, data)
		print(response)
		if is_valid(response):
			print("Response was valid!!")
		else:
			print("Response was not valid.")

def index_data_to_servers(servers, data_file, kReplication):
	rows = get_data(data_file)
	for row in rows:
		# k_servers = servers.get_k_random_servers(kReplication) # TODO: UNCOMMENT THIS
		send_data_to_k_servers(k_servers, "PUT " + row)

def is_server_up(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect((ip, port))
	except:
		return False
	finally:
		sock.close()
		return True

def are_k_server_down(servers, kReplication):
	num_of_down_servers = 0
	for server in servers:
		if not is_server_up(server.get_ip(), server.get_port()):
			num_of_down_servers += 1

		if num_of_down_servers >= kReplication:
			return True
	
	return False

def handle_GET_command(command, servers, kReplication):
	if are_k_server_down(servers, kReplication):
		print("k or more servers are down and therefore it cannot guarantee "
			"the correct output.")
		return
	
	# k_servers = servers.get_k_random_servers(kReplication) # TODO: UNCOMMENT THIS
	send_data_to_k_servers(k_servers, command) # TODO: UNCOMMENT THIS

def handle_user_input(user_input, servers, kReplication):
	command_name = user_input.split(" ")[0]
	if command_name == "GET":
		handle_GET_command(user_input, servers, kReplication)
	elif command_name == "DELETE":
		x = 1 + 1
	elif command_name == "QUERY":
		x = 2 + 2
	else:
		print("unkown command...")

def handle_user_inputs(servers, kReplication):
	# while True:
	user_input = input("KVcmd>")
	handle_user_input(user_input, servers, kReplication)


if __name__ == "__main__":
	args = args.get_args(sys.argv[0], sys.argv[1:])

	k_servers =	[servers.Server(args.ip, args.port)] # TODO: REMOVE THIS

	servers = servers.get_servers(args.serverFile) 

	# index_data_to_servers(servers, args.dataToIndex, args.kFactor)

	handle_user_inputs(k_servers, args.kFactor) # TODO: CHANGE k_server to servers