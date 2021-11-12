list = []
ask = ''
n = 0
while True:
    print('-=-' * 20)
    n = int(input('Enter a number: '))
    if n not in list:
        print('Value successfully registered!')
        list.append(n)
    else:
        print('Duplicated value! Not registered.')
    ask = str(input('Do you wish to continue? [Y/N]: ')).strip().upper()[0]
    if ask in 'N':
            break
print('-=' * 20)
print(f'You have entered the numbers: {sorted(list)}')
