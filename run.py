from minecraft.networking.connection import Connection
import time, random, string, errno
from socket import error as socket_error
from minecraft.networking.packets import *
from threading import Thread

def connection():
        username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12))
        connection = Connection("192.168.2.38", 25565, username=username, initial_version="1.9.4")
        connection.connect()

def main():
	# Contains all thread handlers
	list = []

	# Connect lots of clients to the server
	for i in range(0, 200):
		t = Thread(target = connection)
		t.start()
		list.append(t)

	time.sleep(30)

	# Wait for all threads to be finished
	for t in list:
		t.join()

if __name__ == "__main__":
	main()
