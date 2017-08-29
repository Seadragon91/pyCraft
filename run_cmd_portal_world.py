from minecraft.networking.connection import Connection
import time
from minecraft.networking.packets import *
from threading import Thread
import random
from random import randint

IPAddress = "localhost"
Port = 25565



def connection(a_PlayerName):
	username = a_PlayerName
	connection = Connection(IPAddress, Port, username=username, initial_version="1.10")
	connection.connect()
	
	time.sleep(2)

	packet = ChatPacket()
	
	for i in range(1, 10):
		packet.message = "/portal world"
		connection.write_packet(packet)
		time.sleep(0.01)
		
		packet.message = "/portal world_nether"
		connection.write_packet(packet)
		time.sleep(0.01)


def main():
	# Contains all thread handlers
	list = []

	connection("bot1")

	raw_input("Press a key to abort...")

	# Wait for all threads to be finished
	for t in list:
		t.join()

if __name__ == "__main__":
	main()
