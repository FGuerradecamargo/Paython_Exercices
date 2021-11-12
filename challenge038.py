n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))

if n1 > n2:
    print('\033[1;31mThe first number is bigger!')
elif n1 < n2:
    print('\033[1;31mThe second number is bigger!')
else:
    print('\033[1;31mThere is no bigger number, they are the same!')