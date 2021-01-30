import requests
import re
import base64
import string


def check_if_b64(encrypted):
	match = re.fullmatch(r'^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$', encrypted)
	if match:
		return True
	return False

class DecryptCesar:

	def __init__(self, url, key, encrypted_str):
		if 'https' not in url and 'http' not in url:
			print(f'[-] Invalid url...')
			raise ValueError(f'The specified url |{url}| is not valid')

		if check_if_b64(encrypted_str) is True:
			print(f'[+] Decrypting base64 |{encrypted_str}|')
			encrypted_str = base64.b64decode(encrypted_str).decode('utf-8')

		self.url = url
		self.key = key
		self.encrypted_str = encrypted_str

		self.most_likely = set()
		self.word_dict = {}

	def get_words(self):
		try:
			GET = requests.get(self.url)
			print(f'[+] Making a GET request: {self.url}')

		except requests.exceptions.ConnectionError as ex:
			print('[-] An error occurred...')
			raise ex

		else:
			for e, v in enumerate(re.findall(r'>[a-zA-Z]+</td>', GET.text)):
				stop = v.find('<')
				self.word_dict[v[1:stop]] = e

	@staticmethod
	def decrypt(encrypted, off_set, *, key):
		encrypted = encrypted.lower()
		res = ''

		off_set_dict = {}
		regular_dict = dict(enumerate(string.ascii_lowercase))

		for e, v in enumerate(key):
			off_set_dict[v] = (e + off_set) % 26

		for i in encrypted:
			if i != ' ':
				try:
					res += regular_dict.get(off_set_dict[i])
				except KeyError:
					res += i
			else:
				res += i

		return res

	def brute_force(self):
		count = 0

		for i in range(1, 26):
			for x in DecryptCesar.decrypt(self.encrypted_str, i, key=self.key).split(' '):
				if x in self.word_dict:
					count += 1
			if count > 1:
				self.most_likely.add(self.decrypt(self.encrypted_str, i, key=self.key))
			count = 0

		if not self.most_likely:
			lst = (DecryptCesar.decrypt(self.encrypted_str, i, key=self.key).split(' ') for i in range(1, 26))
			while True:
				enter = input('Enter next to get the next possible result: ')
				print(next(lst)[0])

				if enter != 'next':
					break

		return 'Most likely --> ' + str(self.most_likely).strip('{').strip('}')


def main():
	url = 'https://gist.github.com/deekayen/4148741'

	encrypted = "RlJaRFVHViBHTEggUERRQiBXTFBIViBFSElSVUggV0tITFUgR0hEV0tWOyBXS0ggWURPTERRVyBRSFlIVSBXRFZXSCBSSSBHSERXSyBFWFcgUlFGSC4="
	encrypted_2 = "jxu gkuijyed ev mxujxuh q secfkjuh sqd jxyda yi de cehu ydjuhuijydw jxqd jxu gkuijyed ev mxujxuh q ikrcqhydu sqd imyc."

	test1 = DecryptCesar(url=url, key=string.ascii_lowercase, encrypted_str=encrypted)
	test1.get_words()
	print(test1.brute_force(), end='\n\n')


	test2 = DecryptCesar(url=url, key=string.ascii_lowercase, encrypted_str=encrypted_2)
	test2.get_words()

	print(test2.brute_force())


if __name__ == '__main__':
	main()
