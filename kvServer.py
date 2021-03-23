import sys
import socket
from random import choice
import kv_random as kvr
import arguments as args

MAX_MESSAGE_SIZE = 2048

def handle_PUT_request(conn, request_data):

	conn.sendall(b'OK')

def handle_request(conn, request):
	request_name = request.split(" ")[0]
	request_data = request.split(" ")[1]
	if request_name == "PUT":
		handle_PUT_request(conn, request_data)
	elif request_name == "GET":
		x = 1 + 1
	elif request_name == "DELETE":
		x = 2 + 2
	elif request_name == "QUERY":
		x = 3 + 3
	else:
		print("unkown command...")

def handle_client(conn, addr):
	print('Connected by', addr)

	request = str(conn.recv(MAX_MESSAGE_SIZE))
	if not request:
		return

	print(request)
	handle_request(conn, request)

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