number = int(input('Enter the number that you wish to convert: '))
print('''Chose one of the option bellow to convert:
         [1] Binary
         [2] Octal
         [3] Hexadecimal''')
option = int(input('Your option: '))

if option == 1:
    print('The number {} converted to Binary is: {}'.format(number, bin(number)[2:]))
elif option == 2:
    print('The number {} converted to Octal is: {}'.format(number, oct(number)[2:]))
elif option == 3:
    print('The number {} converted to Hexadecimal is: {}'.format(number, hex(number)[2:]))
else:
    print('\033[1;31m{} is not an option! Please try again.\033[m'.format(option))

