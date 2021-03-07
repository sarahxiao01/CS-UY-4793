
#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket
port_number = 8080
serverSocket.bind(('', port_number))
serverSocket.listen(1)
while True:
	#Establish the connection 
	print('Ready to serve...') 
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024) #Fill in start #Fill in end 
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		#Send one HTTP header line into socket
		#Send the content of the requested file to the client 
		connectionSocket.send("HTTP/1.1 200 OK \r\n\r\n".encode('utf-8'))
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode('utf-8')) 
		connectionSocket.send("\r\n".encode('utf-8'))
		connectionSocket.close() 
	except IOError:
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode('utf-8'))
		connectionSocket.send("\r\n".encode('utf-8'))
		connectionSocket.close() 
		#print("404 File Not Found")
	#Send response message for file not found
#Close client socket
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
