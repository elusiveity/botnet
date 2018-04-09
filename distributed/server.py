# Echo server program
import socket
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# This is the server that sends commands to it's minions.

HOST = config['socket']['host']	# Symbolic name meaning all available interfaces
PORT = int(config['socket']['port'])	# Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(( HOST, PORT ))
s.listen(1)
conn, addr = s.accept()
with conn:
	print('Connected by', addr)
	while True:
		data = conn.recv(1024)
		if not data: break
		conn.sendall(data)
