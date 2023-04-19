import socket
import time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 1337))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            if data := conn.recv(1024):
                print(data.decode())
            else:
                break
        time.sleep(3)
        conn.sendall('This will still be received by the client that has closed its write end'.encode())
