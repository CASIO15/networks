import sys

def _help():
	return 'Usage - python3 <filename.py> <hex to filter> [x01 x02 x03...]'

def bad_chars():
	x = ''

	if len(sys.argv):
		args = [int('0'+i, 16) for i in sys.argv[1:]]

		for i in range(1, 256):
			if len(sys.argv) > 1 and any([True for x in args if i == x]):
				continue
			else:
				x += '\\x{:02x}'.format(i)
	return x

def main():
	if len(sys.argv) == 2 and (sys.argv[1] != '-h' or sys.argv[1] != '--help'):
		print(_help())
	else:
		print(bad_chars())

if __name__ == '__main__':
	main()
