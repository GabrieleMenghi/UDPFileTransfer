import socket as sk
import os, threading

size = 4096
check = True

#Socket creation
socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

#Socket binding
server_address = ('localhost', 10000)
print ('\n\rstarting on %s port %s' % server_address)
socket.bind(server_address)
 
welcome_message = '\r\nUDP file transfer\r\n\r\nOpzioni disponibili\r\n\r\n"list" restituisce la Lista dei file disponibili\r\n"get <filename>" consente di scaricare un file dal server\r\n"put <absolutefilepath>" consente di caricare un file sul server, specificandone il percorso assoluto\r\n"exit" chiude il socket appartenente al client che ha lanciato il comando\r\n'

def listing():
    for i in range(len(os.listdir(os.getcwd()))):
        socket.sendto((os.listdir(os.getcwd()))[i].encode(), address)
        
    socket.sendto(welcome_message.encode(), address)
    
def getting():
    if os.path.exists(data.decode().split()[1]):
        file = open(data.decode().split()[1], "rb")
        send = file.read(size)
        while send:
            socket.sendto(send, address)
            send = file.read(size)
    else:
        socket.sendto('The file does not exists'.encode(), address) 
    socket.sendto(welcome_message.encode(), address)

def putting(filename):
    socket.settimeout(3)
    data, address = socket.recvfrom(size)
    try:
        file = open(filename, "wb")
    except Exception as e:
        socket.sendto(e.encode(), address)
    check = True;
    while check:
        try:
            file.write(data)
            data, server = socket.recvfrom(size)
        except:
            data = None
            if data is not None:
                file.write(data)
            else:
                check = False

    file.close()
    socket.settimeout(None)
    socket.sendto('The file was uploaded succesfully'.encode(), address)
    
while True:
    data, address = socket.recvfrom(size)
    if data.decode() == 'Sending address':
        socket.sendto(welcome_message.encode(), address)
    #List command
    elif data.decode().split()[0] == 'list':
        list_thread = threading.Thread(target=listing)
        list_thread.start()
    #Get command
    elif data.decode().split()[0] == 'get':
        get_thread = threading.Thread(target=getting)
        get_thread.start()
    #Put command
    elif data.decode().split()[0] == 'put':
        path, address = socket.recvfrom(size)
        separate_path = path.decode().split('/')
        #The argument identifies the file name
        put_thread = threading.Thread(target=putting(separate_path[len(separate_path)-1]))
        put_thread.start()