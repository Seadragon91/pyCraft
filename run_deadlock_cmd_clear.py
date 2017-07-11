from minecraft.networking.connection import Connection
import time
from minecraft.networking.packets import *
from threading import Thread
import random
from random import randint

IPAddress = "192.168.2.38"
Port = 25565

players = [ "bot1", "bot2" ]

def connection(a_PlayerName):
	username = a_PlayerName
	connection = Connection(IPAddress, Port, username=username, initial_version="1.10")
	connection.connect()
	
	time.sleep(2)

	packet = ChatPacket()
	
	# Send bot2 to world_nether
	if a_PlayerName == "bot2":
		packet.message = "/portal world_nether"
		connection.write_packet(packet)

		time.sleep(2)
		
		# Clear inventory from bot1 (world) from world_nether
		for i in range(1, 5):
			for i in range(1, 10):
				packet.message = "/clear bot1"
				connection.write_packet(packet)
			time.sleep(2)


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
