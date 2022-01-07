n = (int(input('Enter a number: ')), int(input('Enter a number: ')), int(input('Enter a number: ')), int(input('Enter a number: ')))

print(f'You have entered the numbers: {n}')
print(f'The number 9 appeared {n.count(9)} times')

if 3 in n:
    print(f'The number 3 is in the {n.index(3)+1}º position')
else:
    print('There is no number 3')

print('The even numbers entered is: ', end=' ')

for x in n:
    if x % 2 == 0:
        print(x, end=' > ')
