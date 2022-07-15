import socket as sk
import threading, tkinter
from tkinter import filedialog

size = 4096
check = True

#Socket creation
socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

server_address = ('localhost', 10000)

socket.sendto('Sending address'.encode(), server_address)
data, server = socket.recvfrom(size)
print(data.decode())

def listing():
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

def getting():
    socket.settimeout(3)
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
    socket.settimeout(None)
                
def putting(filepath):
    socket.settimeout(3)
    socket.sendto(filepath.encode(), server_address)
    try:    
        file = open(filepath, "rb")
    except Exception as e:
        print(e)
    send = file.read(size)
    while send:
        #print(send.decode("utf-8"))
        socket.sendto(send, server_address)
        send = file.read(size)
    socket.settimeout(None)
    data, server = socket.recvfrom(size)
    print(data.decode())

while True:
    inp = input()
    socket.sendto(inp.encode(), server)
    #List command
    if inp.split()[0] == 'list':
        list_thread = threading.Thread(target=listing)
        list_thread.start()
    #Get command
    elif inp.split()[0] == 'get':
        get_thread = threading.Thread(target=getting)
        get_thread.start()
    #Put command
    elif inp.split()[0] == 'put':
        #Avoid the appearance of the tkinter window
        tkinter.Tk().withdraw()
        #Open file explorer
        filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File")
        put_thread = threading.Thread(target=putting(filename))
        put_thread.start()

socket.close()