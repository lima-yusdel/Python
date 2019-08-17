import socket
import time
#Stop and Wait packet sending
#By Yusdel Lorenzo YLL15
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8001
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host, port))


serversocket.listen(5)
print ('Sender ready and is listening for receiver to connect')
x = 0
while True:
    #to accept all incoming connections
    clientsocket, address = serversocket.accept()
    try:
        while True:
            message = "Hello:"+str(x)
            clientsocket.send(message.encode())
            data = clientsocket.recv(5)
            ack = (data[-1:].decode())

            if int(x) == int(ack):  #if ACK packet is the one sent then send next packet
                x = x+1
                message = "Hello:"+str(x)
                print(data.decode())
                clientsocket.send(message.encode())
            else:
                if int(ack) == 10:
                    break
    finally:
        # Clean up the connection
        clientsocket.close()
        exit()
