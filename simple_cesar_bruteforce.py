def decrypt(string, off_set, *, key):
	ascii_lower = 'abcdefghijklmnopqrstuvwxyz'

	normal_dict = dict(enumerate(ascii_lower))
	off_set_dict = {}
	res = ''

	for e, v in enumerate(key):
		off_set_dict[v] = (e + off_set) % 26

	for i in string:
		if i != ' ':
			res += normal_dict.get(off_set_dict[i])

		else:
			res += ' '

	return res

def brute_force(string):
	word_list = ['a', 'i', 'me', 'and', 'the', 'it', 'they', 'are', 'if']
	best_options = set()

	for i in range(1, 26):
		for x in decrypt(string, i, key='icghkxpwstujzdleqmbvofanry').split(' '):
			if x in word_list:
				best_options.add(decrypt(string, i, key='icghkxpwstujzdleqmbvofanry'))

	return best_options

print(brute_force("fbyyg ugxym ap l paihyb hxgoxli"))
