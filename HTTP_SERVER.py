import socket, os

def send_file(data, client):

    URL = data.split()[1]

    if URL == '/':

        file = open(r'webroot/index.html', 'rb')
        client.send('HTTP/1.1 200 OK\r\n'.encode())
        client.send(f'Content-Type: text/html; charset=utf-8\r\n'.encode())
        client.send(f'Content-Length: {os.stat("webroot/index.html").st_size}\r\n'.encode())
        client.send('\r\n'.encode())
        client.send(file.read())
        file.close()

    elif URL.endswith('.css'):

        file = open('webroot' + URL, 'rb')
        client.send('HTTP/1.1 200 OK\r\n'.encode())
        client.send(f'Content-Type: text/css\r\n'.encode())
        client.send(f'Content-Length: {os.stat("webroot" + URL).st_size}\r\n'.encode())
        client.send('\r\n'.encode())
        client.send(file.read())
        file.close()

    elif URL.endswith('.jpg'):

        file = open('webroot' + URL, 'rb')
        client.send(r'HTTP/1.1 200 OK\r\n'.encode())
        client.send(f'Content-Type: image/jpeg\r\n'.encode())
        client.send(f'Content-Length: {os.stat("webroot" + URL).st_size}\r\n'.encode())
        client.send('\r\n'.encode())
        client.send(file.read())
        file.close()

    elif URL.endswith('.js'):

        file = open('webroot' + URL, 'rb')
        client.send('HTTP/1.1 200 OK\r\n'.encode())
        client.send(f'Content-Type: text/javascript; charset=utf-8\r\n'.encode())
        client.send(f'Content-Length: {os.stat("webroot" + URL).st_size}\r\n'.encode())
        client.send('\r\n'.encode())
        client.send(file.read())
        file.close()

    elif '/calculate-next' in URL:

        get_num = URL.split('=')
        num = str(int(get_num[-1]) + 1)
        client.send('HTTP/1.1 200 OK\r\n'.encode())
        client.send(f'Content-Type: text/plain; charset=utf-8\r\n'.encode())
        client.send(f'Content-Length: {str(len(num))}\r\n'.encode())
        client.send('\r\n'.encode())
        client.send(str(num).encode())

    else:
        client.send('HTTP/1.1 404 Not Found\r\n'.encode())


def main():

    server = socket.socket()
    server.bind(('0.0.0.0', 80))
    server.listen(10)
    print('SERVER IS RUNNING...')

    while True:
        client, addr = server.accept()
        data = client.recv(1024).decode()

        if 'GET' in data and 'HTTP/1.1' in data:
            send_file(data, client)

        else:
            client.close()


if __name__ == '__main__':
    main()