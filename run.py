from minecraft.networking.connection import Connection
import time, string, errno
from socket import error as socket_error
from minecraft.networking.packets import *
from threading import Thread
import random
from random import randint

IPAddress = "192.168.2.38"
Port = 25565

# Commands that can be run without a argument
commands_no_args = [ "/clear", "/difficulty", "/help", "/kick", "/list", "/listranks", "/motd", "/plugins",
		     "/rank", "/regen", "/save-all", "/seed", "/spawn", "/time", "/time set day",
		     "/time set night", "/toggledownfall", "/weather clear", "/weather thunder", "/weather rain"
		     "/worlds", "/reload" ]

# Commands that require a player name
commands_player_name = [ "/clear", "/kill" ]

# Commands that have more specific arguments
commands_player_name_and_more = [ "/tp", "/portal", "/tell", "/me" ]

# All world names
world_names = [ "world", "world_nether", "world_end" ]

# Gather all commands in one list
all_commands = commands_no_args[:]
all_commands.extend(commands_player_name)
all_commands.extend(commands_player_name_and_more)

players = [ "bot1", "bot2" ] #, "bot3", "bot4", "bot5" ]

def run_command(a_Connection):
	# Get a random command
	# for sCMD in [ "/tell", "/me", "/save-all", "/clear", "/rank", "/listranks" ]:
	# for sCMD in [ "/rank", "/listranks", "/tell", "/clear" ]:
	for sCMD in [ "/tell", "/clear" ]:
		# print sCMD
		iRnd = randint(0, 1)
		packet = ChatPacket()
	
		if sCMD in commands_player_name:
			if iRnd == 0:
				packet.message = sCMD + " " + players[randint(0, len(players) -1)]
			else:
				packet.message = sCMD
		elif sCMD in commands_no_args:
			packet.message = sCMD
		elif sCMD in commands_player_name_and_more:
			if sCMD == "/tp":
				if iRnd == 0:
					# Tp to player
					packet.message = sCMD + " " + players[randint(0, len(players) -1)]
				else:
					# Tp to coords
					packet.message = sCMD + " " + str(randint(-10000, 10000)) + " 100 " + str(randint(-10000, 10000))
			elif sCMD == "/portal":
				# Tp to a random world
				packet.message = sCMD + " " +  world_names[randint(0, len(world_names) -1)]
			elif sCMD == "/tell":
				packet.message = sCMD + " " + players[randint(0, len(players) -1)] + " " + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12))
			elif sCMD == "/me":
				packet.message = sCMD + " " + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12))

		a_Connection.write_packet(packet)

def connection(a_PlayerName):
	username = a_PlayerName #''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12))
	connection = Connection(IPAddress, Port, username=username, initial_version="1.10")
	connection.connect()
	
	time.sleep(2)

	packet = ChatPacket()
	if a_PlayerName == "bot1":
		packet.message = "/portal" + " " + "world"
		connection.write_packet(packet)
	elif a_PlayerName == "bot2":
		packet.message = "/portal" + " " + "world_nether"
		connection.write_packet(packet)
		
		time.sleep(5)
		packet.message = "/tell bot1 1rgki1e0em5r"
		connection.write_packet(packet)
		
		packet.message = "/clear bot1"
		connection.write_packet(packet)
	
	# time.sleep(2)

	# for i in range(1, 5):
	# 	run_command(connection)

def main():
	# Contains all thread handlers
	list = []

	# Connect clients to the server
	for pName in players:
		t = Thread(target = connection, args=(pName,))
		t.start()
		list.append(t)

	raw_input("Press a key to abort...")

	# Wait for all threads to be finished
	for t in list:
		t.join()

if __name__ == "__main__":
	main()
