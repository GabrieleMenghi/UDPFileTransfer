import socket as sk

size = 4096

#Socket creation
socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

server_address = ('localhost', 10000)

message = 'Messaggio di prova'

try:
    socket.sendto(input().encode(), server_address)
    data, server = socket.recvfrom(size)
    print(data.decode())
except Exception as e:
    print(e)
finally:
    socket.close()