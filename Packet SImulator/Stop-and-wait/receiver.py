import socket
import re
import sys, errno
#Stop and Wait packet sending
#By Yusdel Lorenzo YLL15
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8001
s.connect((host,port))
dataList = []
while True:
    try:
        data = s.recv(7)
        if data:
            dataList.append(data.decode())
            digit = data[-1:]
            message ="Ack:"+digit.decode()
            s.send(message.encode())
        if int(digit) == 9:
            break
    except IOError as e:    #if server closes while client sending data, catches error
        if e.errno == errno.EPIPE:
            s.close()
            break
dataset = list(set(dataList)) #gets rid of retransmitted packets received
dataset = sorted(dataset) #sorts the set becuase it messed up the order of the packets

for packet in dataset:
    print(packet)
