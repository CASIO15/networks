from random import sample

# wordlist file.
f = open('password1', 'r').read()

def bruteforce():

    enter = input('Enter a password: ')
    string = ''.join(f.split())
    i = 0
    result = ''

    while result != enter:
        result = ''.join(sample(string, len((enter))))
        i += 1

        if [i for i in enter if i not in string]:
            return 'Letter not in word list.'

        elif enter == result:
            return f'Password: <<- {result} ->> | guess: {i}'

print(bruteforce())
