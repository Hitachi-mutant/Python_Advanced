# Task 1

# import socket

# HOST = '127.0.0.1'  # The server's hostname or IP address
# PORT = 65432        # The port used by the server

# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#     s.connect((HOST, PORT))
#     message = 'message in lower case'.encode()  # Encode to bytes-like object
#     s.sendall(message)
#     data = s.recv(1024)

# print('Received', repr(data))


# Task 2

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def get_encrypted_message(message, key):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                encrypted += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted += char
    return encrypted

key = int(input("Enter the encryption key: "))
message = input("Enter the message to send: ")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    data = f"{key}|{message}"
    s.sendall(data.encode())
    encrypted_data, _ = s.recvfrom(1024)

print('Received encrypted data:', encrypted_data.decode())
