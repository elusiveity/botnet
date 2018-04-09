import socket
import sys
import random

# This is the file I put all my functions into to keep the bot script a little neater
 
class IRC:
 
	irc = socket.socket()
  
	def __init__(self):  
		self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
	def send(self, chan, msg):
		self.irc.send("PRIVMSG " + chan + " :" + msg + "\n\r")

	def whisper(self, user, msg):
		self.irc.send("PRIVMSG " + user + " :" + msg + "\n\r")

	def connect(self, server, channel, botnick):
		print "connecting to:"+server
		self.irc.connect((server, 6667))
		self.irc.send("USER " + botnick + " " + botnick +" " + botnick + " :This is a fun bot! \n")
		self.irc.send("NICK " + botnick + "\n")
		self.irc.send("JOIN " + channel + "\n")
 
	def get_text(self):
		text=self.irc.recv(2040)
 
		if text.find('PING') != -1:
			self.irc.send('PONG ' + text.split() [1] + '\r\n')
 
		return text

def random_line(file):
	lines = open(file).read().splitlines()
	return random.choice(lines)
