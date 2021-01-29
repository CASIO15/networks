key = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(string, off_set, *, key):
	ascii_lower = 'abcdefghijklmnopqrstuvwxyz'

	normal_dict = dict(enumerate(ascii_lower))
	off_set_dict = {}
	res = ''

	for e, v in enumerate(key):
		off_set_dict[v] = (e + off_set) % 26

	for i in string:
		if i != ' ':
			try:
				res += normal_dict.get(off_set_dict[i])
			except KeyError:
				res += i
		else:
			res += i

	return res

def brute_force(string):

	word_list = ['a', 'i', 'me', 'and', 'the', 'it', 'they', 'are', 'if']
	best_options = set()

	for i in range(1, 26):
		for x in decrypt(string, i, key=key).split(' '):
			if x in word_list:
				best_options.add(decrypt(string, i, key=key))

	if not best_options:
		for i in range(1, 26):
			print(decrypt(string, i, key=key))

	return best_options

print(brute_force("FRZDUGV GLH PDQB WLPHV EHIRUH WKHLU GHDWKV; WKH YDOLDQW QHYHU WDVWH RI GHDWK EXW RQFH.".lower()))
# Result: {'cowards die many times before their deaths; the valiant never taste of deathbut once.'}
