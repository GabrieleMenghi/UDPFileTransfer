import socket as sk
import os, threading

size = 4096

#Socket creation
socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

#Socket binding
server_address = ('localhost', 10000)
print ('\n\rstarting on %s port %s' % server_address)
socket.bind(server_address)
 
welcome_message = '\r\nUDP file transfer\r\n\r\nOpzioni disponibili\r\n\r\n"list" restituisce la Lista dei file disponibili\r\n"get <filename>" consente di scaricare un file dal server\r\n"put <filepath> <filename>" consente di caricare un file sul server, specificandone il percorso\r\n'

def list():
    for i in range(len(os.listdir(os.getcwd()))):
        socket.sendto((os.listdir(os.getcwd()))[i].encode(), address)
        
    socket.sendto(welcome_message.encode(), address)
    print(data.decode())
    
def get():
    if os.path.exists(data.decode().split()[1]):
        file = open(data.decode().split()[1], "rb")
        send = file.read(size)
        while send:
            socket.sendto(send, address)
            send = file.read(size)
    else:
        socket.sendto('The file does not exists'.encode(), address) 
    socket.sendto(welcome_message.encode(), address)
    print(data.decode())
    
while True:
    data, address = socket.recvfrom(size)
    if data.decode() == 'Sending address':
        socket.sendto(welcome_message.encode(), address)
    #List command
    elif data.decode().split()[0] == 'list':
        list_thread = threading.Thread(target=list)
        list_thread.start()
    #Get command
    elif data.decode().split()[0] == 'get':
        get_thread = threading.Thread(target=get)
        get_thread.start()
    #Put command
    elif data.decode().split()[0] == 'put':
        socket.sendto('Putting'.encode(), address)
        socket.sendto(welcome_message.encode(), address)
        print(data.decode())