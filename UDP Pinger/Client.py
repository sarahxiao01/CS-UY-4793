
import time 
from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
clientSocket.bind(('127.0.0.1', 12000))
for sequence_num in range(1, 11):
	msg = "Ping " + str(sequence_num) + " " + str(time.strftime("%H:%M:%S"))
	senttime = time.time()
	address = ('127.0.0.1', 12000)
	clientSocket.sendto(msg.encode('utf-8'), address)
	try: 
		rec, address = clientSocket.recvfrom(1024)
		rectime = time.time()
		print "Server reponse: ", rec
		rtt = rectime - senttime 
		print "Round trip time: ", rtt
	except timeout:
		print "Request timed out"