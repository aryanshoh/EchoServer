import socket

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 9091))
sock.listen(10)
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	data = conn.recv(1024)
	if data=='exit':
		break
	msg += data.decode()
	conn.send(data.upper())

print(msg)

conn.close()
