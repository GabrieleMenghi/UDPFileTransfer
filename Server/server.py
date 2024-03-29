import socket as sk
import os, time

size = 4096
check = True
#Avoid packages loss
time_sleep = 0.00000000000000000000000001

#Socket creation
socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

#Socket binding
server_address = ('localhost', 10000)
print ('\n\rstarting on %s, port %s' % server_address)
socket.bind(server_address)
 
welcome_message = '\r\nUDP file transfer\r\n\r\nOpzioni disponibili\r\n\r\n"list" restituisce la Lista dei file disponibili\r\n"get <filename>" consente di scaricare un file dal server\r\n"put" consente di caricare un file sul server, sciegliendolo dal file explorer, che si aprirà dopo aver digitato il comando\r\n"exit" chiude il socket appartenente al client che ha lanciato il comando\r\n'

def listing():
    for i in range(len(os.listdir(os.getcwd()))):
        time.sleep(time_sleep)
        socket.sendto((os.listdir(os.getcwd()))[i].encode(), address)
        
    socket.sendto(welcome_message.encode(), address)
    
def getting():
    if os.path.exists(data.decode().split()[1]):
        socket.sendto('Downloading'.encode(), address) 
        file = open(data.decode().split()[1], "rb")
        send = file.read(size)
        while send:
            time.sleep(time_sleep)
            socket.sendto(send, address)
            send = file.read(size)
        socket.sendto('File succesfully downloaded'.encode(), address)
    else:
        socket.sendto('The file does not exists'.encode(), address) 
    socket.sendto(welcome_message.encode(), address)

def putting(filename, address):
    socket.settimeout(3)
    socket.sendto('Uploading'.encode(), address)
    data1, address = socket.recvfrom(size)
    file = open(filename, "wb")
    check = True;
    while check:
        try:
            file.write(data1)
            data1, server = socket.recvfrom(size)
        except:
            data1 = None
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
        filename = separate_path[len(separate_path)-1]
        if len(filename) > 50:
            filename = filename[len(filename)-50:]
        putting(filename, address)