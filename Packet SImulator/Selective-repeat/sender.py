import socket
import time
import sys, errno
#By Yusdel Lorenzo YLL15
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8001
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host, port))


serversocket.listen(5)
print ('Sender ready and is listening for receiver to connect')
packet = [0,1,2,2,4,3,3,5,6,7,7,7,7,8,9]
#expected results: 0,1,2,4  3,5,6,7  8, 9
i = 0
j = 5
ackCount = 0
ackPackets = []
    #to accept all incoming connections
clientsocket, address = serversocket.accept()
while True:
    if j <= len(packet):
        for x in range(i, j):
            message = "Hello:"+str(packet[i])
            i += 1
            clientsocket.send(message.encode())
        if i == j:
            j = j + 5
    try:
        data = clientsocket.recv(5)
        print(data.decode())
        if data:
            ack = (data[-1:].decode())
            if str(ack).isdigit():
                ackPackets.append(ack)
        if len(ackPackets) == 10:
            break
    except IOError as e:    #if server closes while client sending data, catches error
        if e.errno == errno.EPIPE:
            s.close()
            break
