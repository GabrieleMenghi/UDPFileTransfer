import socket as sk

#Socket creation
socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

#Socket binding
server_address = ('localhost', 10000)
socket.bind(server_address)