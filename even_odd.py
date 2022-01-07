import math
# ask if a number to the user, tell if the number is even or odd
number = int(input('Enter a number: '))
result = number / 2

if result % 2 == 1:
    print('The number {} is odd!'.format(number))

else:
    print('The number {} is even!'.format(number))
