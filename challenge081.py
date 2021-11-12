list = []

while True:
    list.append(int(input('Enter a number: ')))
    ask = ' '
    while ask not in 'YyNn':
        ask = str(input('Do you wish to continue? [Y/N]: ')).strip()[0]
    if ask in 'Nn':
        break
print('=-=' * 20)
print(f'You have entered {len(list)} number.')
print(f'The number entered in descending order  are: {sorted(list, reverse=True)}')
if 5 in list:
    print(f'You have entered the number 5, it is in the position', end=' ')
    for i, v in enumerate(list):
        if v == 5:
            print(f'{i}', end='...')
else:
    print('You did not entered the number 5! It is not in the list!')