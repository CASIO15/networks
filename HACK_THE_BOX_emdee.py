import requests
import hashlib

url = input('Enter URL and Port: ')
url = 'http://' + url + '/'

session_1 = requests.session()

GET = session_1.get(url)
print('[+] SEND GET...')

sha_key_start = GET.text.find("<h3 align='center'>")
sha_key_end = GET.text.find("</h3")
sha_key = GET.text[sha_key_start+19:sha_key_end]

print(f'[+] FIND KEY {sha_key}')

sha_encrypt_res = hashlib.md5(sha_key.encode()).hexdigest()
print(f'[+] KEY IS ENCRYPTED {sha_encrypt_res}\n')

data = {'hash': sha_encrypt_res}

POST = session_1.post(url, data=data)

print(POST.text)

##### Another solution using sockets #####

import socket
import re
import hashlib

addr = enter your session ip
port = enter your session port

def start_connection():
    client = socket.socket()
    client.connect((addr, port))
    return client

def GET_req():

    client = start_connection()
    GET = 'GET / HTTP/1.1\r\nHost: {0}:{1}\r\n\r\n'.format(addr, port)

    client.send(GET.encode())
    print('[+] Sending GET\n')

    DATA = client.recv(4096).decode()
    client.close()

    extract_data(DATA)

def POST_req(data, session):

    client = start_connection()

    content_type = "application/x-www-form-urlencoded"
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"
    content_length = len("hash=" + str(data))

    POST = "POST / HTTP/1.1\r\nHOST: {host}:{port}\r\nContent-Type: {content_type}\r\nUser-Agent: {agent}\r\nCookie: {cookie}\r\nContent-Length: {content_length}\r\n\r\nhash={hash}".format(
        host=addr, port=port, content_type=content_type,
        agent=user_agent, cookie=session, content_length=content_length, hash=data)

    client.send(POST.encode())
    print('[+] Sending POST\n')

    result = client.recv(4096).decode()
    client.close()

    flag = re.findall('HTB{[A-Za-z0-9_!]+}', result)
    print('Your flag is:', flag[0])

def extract_data(data):

    cookie_start = data.find("PHPSESSID=")
    cookie_end = data.find(";")
    cookie = data[cookie_start:cookie_end]

    hash_start = data.find("<h3 align='center'>")
    hash_end = data.find("</h3>")

    key = data[hash_start + 19:hash_end]

    md5 = hashlib.md5()
    md5.update(key.encode())

    key = md5.hexdigest()

    print('Got Cookie', cookie)
    print('Key is encrypted', key, '\n')

    POST_req(key, cookie)

GET_req()
