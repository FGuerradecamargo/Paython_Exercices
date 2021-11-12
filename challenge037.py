n = int(input('Enter a number: '))
print('''Chose one of the option bellow to convert:
[1] Binary
[2] Octal
[3] Hexadecimal''')
o = int(input('Your option: '))

if o == 1:
    print('The number {} converted to Binary is: {}'.format(n, bin(n)[2:]))
elif o == 2:
    print('The number {} converted to Octal is: {}'.format(n, oct(n)[2:]))
elif o == 3:
    print('The number {} converted to Hexadecimal is: {}'.format(n, hex(n)[2:]))
else:
    print('\033[1;31m{} is not an option! Please try again.\033[m'.format(o))
