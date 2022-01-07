number = int(input('Enter a number to know its factorial: '))
factorial = number

while number != 1:
    factorial = factorial * (number - 1)
    number -= 1

print(f'{number}! = {factorial}')
