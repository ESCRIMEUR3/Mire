# ----- An UDP server in Python that receives temperature values from clients-----

import socket

import datetime

 

# Define the IP address and the Port Number

ip      = "127.0.0.1"

port    = 7070

listeningAddress = (ip, port)

 

# Create a datagram based server socket that uses IPv4 addressing scheme

datagramSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

datagramSocket.bind(listeningAddress)

 

while(True):

    tempVal, sourceAddress = datagramSocket.recvfrom(128)

    print("Temperature at %s is %s"%(sourceAddress, tempVal.decode()))

    response = "Received at: %s"%datetime.datetime.now()

    datagramSocket.sendto(response.encode(), sourceAddress)