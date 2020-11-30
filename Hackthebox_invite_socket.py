import socket
import ssl

client = socket.socket()

with client as c:
	addr = socket.gethostbyname('www.hackthebox.eu')
	c.connect((addr, 443))
	
	c_ssl = ssl.wrap_socket(c, ssl_version=ssl.PROTOCOL_SSLv23)
	
	c_ssl.send(b'POST https://www.hackthebox.eu/api/invite/generate HTTP/1.1\r\n')
	
	c_ssl.send(b'Content-type: application/json; charset=utf-8\r\n')
	
	c_ssl.send(b'User-agent: Mozilla 5.0\r\n')
	
	c_ssl.send(b'Connection: close\r\n')
	
	c_ssl.send('Host: www.hackthebox.eu:443\r\n'.encode())
	
	c_ssl.send(b'\r\n')
	
	data = c_ssl.makefile()
	
	for i in data.readlines():
		if 'code' in i:
			print(i)
	
