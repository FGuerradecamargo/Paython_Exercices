answer = ''
list = []
counter = 0

while answer != 'N':
    n = int(input('Enter a number: '))
    answer = str(input('Do you wish to continue? [S/N]: ')).strip().upper()[0]
    list.append(n)
    counter += 1

print('-' *40)
print(f'You have entered {counter} numbers\nThe average number is: {sum(list) / counter}')
print(f'The higher number is {max(list)} and the lower is {min(list)}')