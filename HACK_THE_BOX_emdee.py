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
