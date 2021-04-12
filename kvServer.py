import sys
import socket
from random import choice
import kv_random as kvr
import arguments as args
import trie

MAX_MESSAGE_SIZE = 1024*1000

trie = trie.Trie()

def string_to_bytes(data):
	return bytes(data, "ascii")

def parse_PUT_request_data(request):
	request = "".join(request.split())

	i = request.index(":")
	key, value = request[ : i], request[i+1 : ]

	return key.replace("\"", ""), value

def handle_PUT_request(conn, request_data):
	key, value = parse_PUT_request_data(request_data)
	trie.put(key, value)

	conn.sendall(b'OK')

def handle_GET_request(conn, key):
	response = trie.get(key)
	if response == None:
		response = "NOT FOUND"
	else:
		response = key + " : " + response

	conn.sendall(string_to_bytes(response))

def handle_DELETE_request(conn, request_data):
	request_data = request_data.replace("\"", "")

	response = trie.delete(request_data)
	if response == None:
		response = "NOT FOUND"
	else:
		response = "OK"

	conn.sendall(string_to_bytes(response))

def handle_QUERY_request(conn, key_path):
	response = trie.query(key_path)
	if response == None:
		response = "NOT FOUND"
	else:
		response = key_path + " : " + response

	conn.sendall(string_to_bytes(response))

def parse_request(request):
	i = request.index(" ")
	return request[ : i], request[i+1 : ]

def handle_request(conn, request):
	request_name, request_data = parse_request(request)

	if request_name == "PUT":
		handle_PUT_request(conn, request_data)
	elif request_name == "GET":
		handle_GET_request(conn, request_data)
	elif request_name == "DELETE":
		handle_DELETE_request(conn, request_data)
	elif request_name == "QUERY":
		handle_QUERY_request(conn, request_data)
	else:
		print("unknown command...")

def bytes_to_string(data):
	return data.decode()

def handle_client(conn, addr):
	print('Connected by', addr)

	request = conn.recv(MAX_MESSAGE_SIZE)
	if not request:
		return

	request = bytes_to_string(request)
	print(request)

	handle_request(conn, str(request))

def run_server(ip, port):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		print("running on:", ip, port)
		s.bind((ip, port))
		s.listen()

		while True:
			conn, addr = s.accept()
			with conn:
				handle_client(conn, addr)

if __name__ == "__main__":
	args = args.get_args(sys.argv[0], sys.argv[1:])

	run_server(args.ip, args.port)