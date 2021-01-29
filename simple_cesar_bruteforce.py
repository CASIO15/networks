import requests
import re

class DecryptCesar:

	def __init__(self, url, key, enctypted_str):
		if 'https' not in url and 'http' not in url:
			print(f'[-] Invalid url...')
			raise ValueError(f'The specified url |{url}| is not valid')

		self.url = url
		self.key = key
		self.encrypted_str = enctypted_str

		self.highest_chance = set()
		self.word_dict = {}

	def get_words(self):
		GET = requests.get(self.url)
		print(f'[+] Making a GET from: {self.url}')
		for e, v in enumerate(re.findall(r'>[a-zA-Z]+</td>', GET.text)):
			stop = v.find('<')
			self.word_dict[v[1:stop]] = e

	@staticmethod
	def decrypt(encrypted, off_set, *, key):
		encrypted = encrypted.lower()
		res = ''

		off_set_dict = {}
		regular_dict = dict(enumerate('abcdefghijklmnopqrstuvwxyz'))

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
				self.highest_chance.add(self.decrypt(self.encrypted_str, i, key=self.key))

			count = 0

		if not self.highest_chance:
			for i in range(1, 26):
				print(self.decrypt(self.encrypted_str, i, key=self.key))

		return 'Most likely --> ' + str(self.highest_chance).strip('{').strip('}')


def main():

	key = 'abcdefghijklmnopqrstuvwxyz'
	url = 'https://gist.github.com/deekayen/4148741'
	encrypted = "FRZDUGV GLH PDQB WLPHV EHIRUH WKHLU GHDWKV; WKH YDOLDQW QHYHU WDVWH RI GHDWK EXW RQFH."

	test1 = DecryptCesar(url=url, key=key, enctypted_str=encrypted)
	test1.get_words()
	print(test1.brute_force())

	# Result: {'cowards die many times before their deaths; the valiant never taste of death but once.'}

if __name__ == '__main__':
	main()
