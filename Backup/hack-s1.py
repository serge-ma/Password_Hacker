# Password Hacker: Stage 1/5
# https://hyperskill.org/projects/80/stages/442/implement

import sys
import socket

address = (sys.argv[1], int(sys.argv[2]))
message = sys.argv[3].encode()

with socket.socket() as client_socket:
    client_socket.connect(address)
    client_socket.send(message)
    response = client_socket.recv(1024).decode()
    print(response)
