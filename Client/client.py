import socket as sk
import threading

size = 4096
check = True

#Socket creation
socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

server_address = ('localhost', 10000)

socket.sendto('Sending address'.encode(), server_address)
data, server = socket.recvfrom(size)
print(data.decode())

socket.settimeout(3)

def list():
    check = True;
    while check:
        try:
            data, server = socket.recvfrom(size)
        except:
            data = None
        if data is not None:
            print(data.decode())
        else:
            check = False

def get():
    data, server = socket.recvfrom(size)
    if data.decode() != 'The file does not exists':
        file = open(inp.split()[1], "wb")
        check = True;
        while check:
            if data.decode().split()[0] != 'UDP':
                try:
                    file.write(data)
                    data, server = socket.recvfrom(size)
                except:
                    data = None
                    if data is not None:
                        file.write(data)
                    else:
                        check = False
            else:
                print(data.decode())
                check = False
        file.close()
    else:
        print(data.decode())
        check = True;
        while check:
            try:
                data, server = socket.recvfrom(size)
            except:
                data = None
            if data is not None:
                print(data.decode())
            else:
                check = False

while True:
    inp = input()
    socket.sendto(inp.encode(), server)
    """check = True;
    while check:
        try:
            data, server = socket.recvfrom(size)
        except:
            data = None
        if data is not None:
            print(data.decode())
        else:
            check = False;"""
    #List command
    if inp.split()[0] == 'list':
        list_thread = threading.Thread(target=list)
        list_thread.start()
    #Get command
    elif inp.split()[0] == 'get':
        get_thread = threading.Thread(target=get)
        get_thread.start()

socket.close()