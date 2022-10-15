import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('10.4.33.66', 9091))
msg=''
while msg!='exit':
    msg = input('Enter data ')
    if msg!='exit':
        msg+='\n'
    sock.send(msg.encode())
    data = sock.recv(1024)

sock.close()
