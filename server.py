#the server

import os
from socket import *
host = "192.168.10.20" #example ip host
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print "Waiting messages..."
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    print "Received: " + data
    if data == "exit":
        break
UDPSock.close()
os._exit(0)

