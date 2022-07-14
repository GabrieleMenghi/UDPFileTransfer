import socket as sk
import threading, os

size = 4096

#Socket creation
socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

#Socket binding
server_address = ('localhost', 10000)
print ('\n\rstarting on %s port %s' % server_address)
socket.bind(server_address)

lock = threading.Lock()
 
welcome_message = '\r\nUDP file transfer\r\n\r\nOpzioni disponibili\r\n\r\n"list" restituisce la Lista dei file disponibili\r\n"get <filename>" consente di scaricare un file dal server\r\n"put <filepath> <filename>" consente di caricare un file sul server, specificandone il percorso\r\n'

"""
class daemon(threading.Thread):
    def __init__(self, a):
        threading.Thread.__init__(self)
        self.socket = a[0]
        self.address = a[1]
    def run(self):
        #Show welcome message
        sent = self.socket.sendto(welcome_message.encode(), server_address[0])
        print(sent)
        #TODO manage different commands
        #while(True):
        self.socket.close()
            
     
while True:
    daemon(socket.accept()).start()

"""
while True:
    data, address = socket.recvfrom(size)
    if data.decode() == 'Sending address':
        socket.sendto(welcome_message.encode(), address)
    elif data.decode().split()[0] == 'list':
        for i in range(len(os.listdir(os.getcwd()))):
            socket.sendto((os.listdir(os.getcwd()))[i].encode(), address)
            
        socket.sendto(welcome_message.encode(), address)
        print(data.decode())
    elif data.decode().split()[0] == 'get':
        if os.path.exists(data.decode().split()[1]):
            #socket.sendto('Exists'.encode(), address)
            file = open(data.decode().split()[1], "rb")
            send = file.read(size)
            while send:
                socket.sendto(send, address)
                send = file.read(size)
        else:
            socket.sendto('The file does not exists'.encode(), address) 
        socket.sendto(welcome_message.encode(), address)
        print(data.decode())
    elif data.decode().split()[0] == 'put':
        socket.sendto('Putting'.encode(), address)
        socket.sendto(welcome_message.encode(), address)
        print(data.decode())