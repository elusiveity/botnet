import random

#I decided to keep this random line script separate incase I needed it again.

def randomLine(file):
	lines = open(file).read().splitlines()
	return random.choice(lines)

print randomLine('dirty-talk.txt')
