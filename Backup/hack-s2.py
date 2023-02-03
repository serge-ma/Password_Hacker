# Password Hacker: Stage 2/5
# https://hyperskill.org/projects/80/stages/443/implement

import sys
import socket
import itertools
import string

address = (sys.argv[1], int(sys.argv[2]))
password_chars = string.ascii_lowercase + string.digits


def password_gen():
    for length in range(1, 10):
        for text in itertools.product(password_chars, repeat=length):
            yield ''.join(text)


with socket.socket() as client_socket:
    client_socket.connect(address)
    for password in password_gen():
        client_socket.send(password.encode())
        response = client_socket.recv(1024).decode()
        if response == 'Connection success!':
            print(password)
            break
