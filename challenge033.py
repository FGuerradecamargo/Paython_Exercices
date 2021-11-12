# ask three numbers to the user, show with one is the bigger and the smaller
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))
list = [n1, n2, n3]

print('The bigger number is: {}'.format(max(list)))
print('The smaller number is: {}'.format(min(list)))
