'''Home work for the lesson 32'''

'''Task 1 - During the lesson, we have created a server and client, which use TCP/IP protocol for communication via sockets. 
In this task, you have to create a server and client, which will use user datagram protocol (UDP) for communication.'''
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

# the response will be sent back to the client.py (location ~Python_Advanced/server)

'''Task 2 - Extend the echo server, which returns to client the data, encrypted using the Caesar 
cipher algorithm by a specific key obtained from the client.'''



import socket

def caesar_encrypt(text, key):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                encrypted += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted += char
    return encrypted

HOST = '127.0.0.1'
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (HOST, PORT)
sock.bind(server_address)

while True:
    data, addr = sock.recvfrom(1024)
    if not data:
        break
    
    key, message = data.decode().split('|')
    key = int(key)
    
    encrypted_message = caesar_encrypt(message, key)
    sock.sendto(encrypted_message.encode(), addr)

print('Data were sent to:', addr)
sock.close()

# the response will be sent back to the client.py (location ~Python_Advanced/server)