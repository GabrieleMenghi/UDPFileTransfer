import socket as sk
from tkinter import *
from tkinter import filedialog
import time

size = 4096
check = True
#Avoid packages loss
time_sleep = 0.00000000000000000000000001

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
    data1, server = socket.recvfrom(size)
    if data1 != 'The file does not exists'.encode():
        file = open(inp.split()[1], "wb")
        check = True;
        while check:
            if data1 == 'Downloading'.encode():
                print(data1.decode())
                data1, server = socket.recvfrom(size)
            else:
                if data1 == 'File succesfully downloaded'.encode():
                    print(data1.decode())
                    check = False
                else:
                    file.write(data1)
                    data1, server = socket.recvfrom(size)
        data1, server = socket.recvfrom(size)
        if data1 == data0:
            print(data1.decode())
        file.close()
    else:
        socket.settimeout(3)
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
        time.sleep(time_sleep)
        socket.sendto(send, server_address)
        send = file.read(size)
    socket.settimeout(5)
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
    
def openFile():
    global fname
    fname = filedialog.askopenfilename(initialdir = "/",
                                       title = "Select a File")
    root.destroy()

while True:
    inp = input()
    #List command
    if inp.split()[0] == 'list':
        socket.sendto(inp.encode(), server)
        listing()
    #Get command
    elif inp.split()[0] == 'get':
        socket.sendto(inp.encode(), server)
        getting()
    #Put command
    elif inp.split()[0] == 'put':
        root = Tk()
        Button(root, text='Open file explorer', command = openFile).pack(fill=X)
        root.mainloop()

        if fname:
            socket.sendto(inp.encode(), server)
            putting(fname)
        else:
            print('No file was selected')
    elif inp.split()[0] == 'exit':
        break
    
socket.close()