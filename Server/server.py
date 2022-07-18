import socket as sk
import os, threading
import time

size = 4096
check = True

#Socket creation
socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

#Socket binding
server_address = ('localhost', 10000)
print ('\n\rstarting on %s port %s' % server_address)
socket.bind(server_address)
 
welcome_message = '\r\nUDP file transfer\r\n\r\nOpzioni disponibili\r\n\r\n"list" restituisce la Lista dei file disponibili\r\n"get <filename>" consente di scaricare un file dal server\r\n"put" consente di caricare un file sul server, sciegliendolo dal file explorer, che si aprirà dopo aver digitato il comando\r\n"exit" chiude il socket appartenente al client che ha lanciato il comando\r\n'

def listing():
    for i in range(len(os.listdir(os.getcwd()))):
        socket.sendto((os.listdir(os.getcwd()))[i].encode(), address)
        
    socket.sendto(welcome_message.encode(), address)
    
def getting():
    if os.path.exists(data.decode().split()[1]):
        file = open(data.decode().split()[1], "rb")
        send = file.read(size)
        while send:
            time.sleep(0.00000000000000000000000001)
            socket.sendto(send, address)
            send = file.read(size)
        #socket.sendto('File succesfully downloaded', address)
    else:
        socket.sendto('The file does not exists'.encode(), address) 
    socket.sendto(welcome_message.encode(), address)

def putting(filename):
    socket.settimeout(3)
    data1, address = socket.recvfrom(size)
    try:
        file = open(filename, "wb")
    except Exception as e:
        socket.sendto(e.encode(), address)
    check = True;
    while check:
        try:
            file.write(data1)
            data1, server = socket.recvfrom(size)
        except:
            data1 = None
            if data1 is not None:
                file.write(data1)
            else:
                check = False

    file.close()
    socket.sendto('The file was uploaded succesfully'.encode(), address)
    socket.sendto(welcome_message.encode(), address)
    socket.settimeout(None)
    
while True:
    data, address = socket.recvfrom(size)
    if data.decode() == 'Sending address':
        socket.sendto(welcome_message.encode(), address)
    #List command
    elif data.decode().split()[0] == 'list':
        listing()
    #Get command
    elif data.decode().split()[0] == 'get':
        getting()
    #Put command
    elif data.decode().split()[0] == 'put':
        path, address = socket.recvfrom(size)
        separate_path = path.decode().split('/')
        #The argument identifies the file name
        putting(separate_path[len(separate_path)-1])