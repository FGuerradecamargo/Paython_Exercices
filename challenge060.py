n = int(input('Enter a number to know its factorial: '))
n1 = n
factorial = n1
while n1 != 1:
    factorial = factorial * (n1 - 1)
    n1 = n1 - 1

print(f'{n}! = {factorial}')
