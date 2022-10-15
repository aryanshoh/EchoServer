import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9091))

while msg!='exit':
    msg = input('Enter data ')
    if msg!='exit':
        msg+='\n'
    sock.send(msg.encode())
    data = sock.recv(1024)

sock.close()

print(data.decode())
