# ----- An UDP client in Python that sends temperature values to server-----

import socket

import random

 

# Get temperature

def getTemp():

    temp = random.uniform(60.0, 62.0)

    return temp

 

# A tuple with server ip and port

serverAddress = ("127.0.0.1", 7070)

 

# Create a datagram socket

tempSensorSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 

# Get temperature

temperature = getTemp()

tempString  = "%.2f"%temperature

 

# Socket is not in connected state yet...sendto() can be used

# Send temperature to the server

tempSensorSocket.sendto(tempString.encode(), ("127.0.0.1",7070))

 

# Read UDP server's response datagram

response = tempSensorSocket.recv(1024)

print(response)