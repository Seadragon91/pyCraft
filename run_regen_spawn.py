from minecraft.networking.connection import Connection
import time
from minecraft.networking.packets import ChatPacket
from threading import Thread

IPAddress = "127.0.0.1"
Port = 25565

players = [ "bot1", "bot2" ]

def connection(a_PlayerName):
	username = a_PlayerName
	connection = Connection(IPAddress, Port, username=username)
	connection.connect()
	
	time.sleep(2)
	
	packet = ChatPacket()	
	for i in range(1, 10):
		packet.message = "/regen"
		connection.write_packet(packet)
		time.sleep(0.1)
		
		packet.message = "/spawn"
		connection.write_packet(packet)
		time.sleep(0.1)

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
