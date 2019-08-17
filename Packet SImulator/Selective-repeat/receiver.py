import socket
import re
import sys, errno
#By Yusdel Lorenzo YLL15
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8001
s.connect((host,port))
dataList = []
allData = []
received = []
dataPrint = []
seqNumbers = [(0, False), (1, False), (2, False), (3, False), (4, False), (5, False), (6, False), (7, False), (8, False), (9, False)]
#0,1,2,4    3,5,6,7    8,9
seqNumbers = dict(seqNumbers)
while True:
    try:
        data = s.recv(7)
        if data:
            digit = int(data[-1:].decode())
            allData.append(data.decode())
            for x in seqNumbers:
                if digit == x and seqNumbers[x] == False:
                        message = "Ack:" + str(digit)
                        s.send(message.encode())
                        print(data.decode())
                        received.append(digit)
                        seqNumbers[x] = True
        if len(received) == 10:
            break
        if (len(allData) % 5 == 0):
            print("     ")
            message = "     "
            s.send(message.encode())
    except IOError as e:    #if server closes while client sending data, catches error
        if e.errno == errno.EPIPE:
            s.close()
            break
