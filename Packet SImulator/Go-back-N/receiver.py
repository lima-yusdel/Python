import socket
import re
import sys, errno
#By Yusdel Lorenzo YLL15
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8001
s.connect((host,port))
dataList = []
received = []
dataPrint = []
seqNum = 0
while True:
    try:
        data = s.recv(7)
        if data:
            digit = int(data[-1:].decode())
            if digit == seqNum:
                message = "Ack:" + str(digit)
                s.send(message.encode())
                print(data.decode())
                received.append(digit)
                seqNum = seqNum + 1
            else:
                print(" ")
                message = "     "
                s.send(message.encode())
        if len(received) == 10:
            break
    except IOError as e:    #if server closes while client sending data, catches error
        if e.errno == errno.EPIPE:
            s.close()
            break
