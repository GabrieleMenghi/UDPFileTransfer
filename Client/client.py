import socket as sk

size = 4096
check = True

#Socket creation
socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

server_address = ('localhost', 10000)

socket.sendto('Sending address'.encode(), server_address)
data, server = socket.recvfrom(size)
print(data.decode())


socket.settimeout(3)
while True:
    socket.sendto(input().encode(), server)
    check = True;
    while check:
        try:
            data, server = socket.recvfrom(size)
        except:
            data = None
        if data is not None:
            print(data.decode())
        else:
            check = False;

socket.close()