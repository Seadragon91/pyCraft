from minecraft.networking.connection import Connection
import time, string, errno
from socket import error as socket_error
from minecraft.networking.packets import *
from threading import Thread
import random
from random import randint

IPAddress = "localhost" # "192.168.2.38"
Port = 25565

def connection(a_PlayerName):
	username = a_PlayerName #''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12))
	connection = Connection(IPAddress, Port, username=username, initial_version="1.10")
	connection.connect()

	time.sleep(5)

    # packet = ChatPacket()
    # packet.message = "/portal" + " " + "world_nether"
	# connection.write_packet(packet)


	# packet = ChatPacket()
	# if a_PlayerName == "bot1":
	# 	packet.message = "/portal" + " " + "world"
	# 	connection.write_packet(packet)
	# elif a_PlayerName == "bot2":
	# 	packet.message = "/portal" + " " + "world_nether"
	# 	connection.write_packet(packet)
	#
	# 	time.sleep(5)
	# 	packet.message = "/tell bot1 1rgki1e0em5r"
	# 	connection.write_packet(packet)
	#
	# 	packet.message = "/clear bot1"
	# 	connection.write_packet(packet)

	# time.sleep(2)

	# for i in range(1, 5):
	# 	run_command(connection)

def main():
	# Contains all thread handlers
	list = []

	# Connect clients to the server
	for i in range(1, 100):
		pName = "bot" + str(i)
		t = Thread(target = connection, args=(pName,))
		t.start()
		list.append(t)

	# for pName in players:
	# 	t = Thread(target = connection, args=(pName,))
	# 	t.start()
	# 	list.append(t)

	raw_input("Press a key to abort...")

	# Wait for all threads to be finished
	try:
		for t in list:
			t.join()
	except:
		pass

if __name__ == "__main__":
	main()
