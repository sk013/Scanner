#!/usr/bin/python

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("[*]Enter the host to scan")
port = 80
def portscanner(port):
	if sock.connect_ex((host,port)):
		print(colored("port %d is closed" % (port),'red'))
	else:
		print(colored("port %d is open" %(port),'green'))
portscanner(port)
#for port in range(1,1000):
#	portscanner(port)
