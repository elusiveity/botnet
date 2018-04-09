from irc import *
import os
import random
import re
import logging

# This is the runnin gbot. 
# Simply run this to do things.
 
channel = "#bottest"
server = "irc.freenode.net"
nickname = "byouruser"
 
irc = IRC()
irc.connect(server, channel, nickname)

logging.basicConfig(filename='log.txt', level=logging.DEBUG)
 
 
while 1:
	text = irc.get_text()
	cmdmsg = text.split(" ", 1)
	#if len(text) > 0:
	#if len(	print "+"+text
	logging.info(cmdmsg)
 
	if "PRIVMSG" in text and channel in text and ":hello" in text:
		print "Found hello"
		irc.send(channel, "Hello!")

	if "PRIVMSG" in cmdmsg[1] and channel in cmdmsg[1] and '.seen' in cmdmsg[1]:
		irc.send(channel, "Who do you want to see?")

	if "PRIVMSG" in cmdmsg[1] and nickname in cmdmsg[1] and 'talk dirty to me' in cmdmsg[1]:
		irc.whisper('youruser', random_line('dirty-talk.txt'))
		
