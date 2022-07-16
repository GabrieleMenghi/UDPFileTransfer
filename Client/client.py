import socket as sk
import threading, tkinter
from tkinter import filedialog

size = 4096
check = True

#Socket creation
socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

server_address = ('localhost', 10000)

socket.sendto('Sending address'.encode(), server_address)
data0, server = socket.recvfrom(size)
print(data0.decode())

def listing():
    socket.settimeout(2)
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

def getting():
    socket.settimeout(3)
    data1, server = socket.recvfrom(size)
    if data1 != 'The file does not exists'.encode():
        file = open(inp.split()[1], "wb")
        check = True;
        if data1 != data0:
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
        else:
            print(data1.decode())
    else:
        print(data1.decode())
        check = True;
        while check:
            try:
                data1, server = socket.recvfrom(size)
            except:
                data1 = None
            if data1 is not None:
                print(data1.decode())
            else:
                check = False
    socket.settimeout(None)
                
def putting(filepath):
    socket.sendto(filepath.encode(), server_address)
    try:    
        file = open(filepath, "rb")
    except Exception as e:
        print(e)
    send = file.read(size)
    while send:
        socket.sendto(send, server_address)
        send = file.read(size)
    socket.settimeout(6)
    check = True;
    while check:
        try:
            data2, server = socket.recvfrom(size)
        except:
            data2 = None
        if data2 is not None:
            print(data2.decode())
        else:
            check = False
    socket.settimeout(None)

while True:
    inp = input()
    socket.sendto(inp.encode(), server)
    #List command
    if inp.split()[0] == 'list':
        """list_thread = threading.Thread(target=listing)
        list_thread.start()"""
        listing()
    #Get command
    elif inp.split()[0] == 'get':
        """get_thread = threading.Thread(target=getting)
        get_thread.start()"""
        getting()
    #Put command
    elif inp.split()[0] == 'put':
        #Avoid the appearance of the tkinter window
        tkinter.Tk().withdraw()
        #Open file explorer
        filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File")
        """put_thread = threading.Thread(target=putting(filename))
        put_thread.start()"""
        putting(filename)

socket.close()