# Password Hacker: Stage 3/5
# https://hyperskill.org/projects/80/stages/444/implement

import os
import sys
import socket
import itertools

address = (sys.argv[1], int(sys.argv[2]))

with open(os.path.join(os.path.dirname(__file__), 'passwords.txt'), "r", encoding="utf-8") as file:
    passwords = file.read().split()


def password_gen():
    for word in passwords:
        zipped = zip(word.lower(), word.upper())
        for case in set(itertools.product(*zipped)):
            yield ''.join(case)


with socket.socket() as client_socket:
    client_socket.connect(address)
    for password in password_gen():
        client_socket.send(password.encode())
        response = client_socket.recv(1024).decode()
        if response == 'Connection success!':
            print(password)
            break
