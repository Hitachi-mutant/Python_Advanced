import socket

HOST = '127.0.0.1'
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (HOST, PORT)
sock.bind(server_address)

while True:
    data, addr = sock.recvfrom(1024)
    if not data:
        break
    sock.sendto(data.upper(), addr)

sock.close()
