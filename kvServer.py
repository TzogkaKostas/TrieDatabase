import sys
import socket
from random import choice
import kv_random as kvr
import arguments as args

MAX_MESSAGE_SIZE = 2048

def handle_client(conn, addr):
	print('Connected by', addr)

	data = conn.recv(MAX_MESSAGE_SIZE)
	if not data:
		return

	print(data)

	conn.sendall(b'OK')

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