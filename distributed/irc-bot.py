# Echo client program
import socket
import sys
import random
import configparser

config = configparser.ConfigParser()
config.read('config.ini');

# This bot should communicate with the server.
# This is for connecting to IRC and talking to you

# Open the socket for communication
# We use the config files data for this connection
HOST = config['socket']['host']
PORT = int(config['socket']['port'])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(( HOST, PORT ))
s.sendall(b'Hello, world')
data = s.recv(1024)
print('Received', repr(data))
