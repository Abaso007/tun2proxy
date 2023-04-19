import socket
import time
import sys

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    ip, port = sys.argv[1].split(':', 1)
    port = int(port)
    s.connect((ip, port))
    s.sendall('I am closing the write end, but I can still receive data'.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        if data := s.recv(1024):
            print(data.decode())
        else:
            break
