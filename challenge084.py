list = list()
list_temp = []
higher = lower = v1 = 0
heavier = []
lighter = []
while True:
    list_temp.append(str(input('Enter your name: ')).strip().upper())
    list_temp.append(float(input('Enter your weight: ')))
    list.append(list_temp[:])
    list_temp.clear()
    ask = ' '
    while ask not in 'YyNn':
        ask = str(input('Do you wish to continue? [N/Y]: '))
    if ask in 'Nn':
        break

for i, v in list:
    if higher == 0:
        higher = lower = v
        heavier.append(i)
        lighter.append(i)
    else:
        if v > higher:
            higher = v
            heavier.clear()
            heavier.append(i)
            v1 = v
        elif v == higher:
            higher = v
            heavier.append(i)

        if v < lower:
            lower = v
            lighter.clear()
            lighter.append(i)
        elif v == lower:
            lower = v
            lighter.append(i)
print('=' * 60)
print(f'{len(list)} people')
print(f'The highest record weight was: {higher} Kg,', end=' ')
print(f'from {heavier}')
print(f'The lowest record weight was: {lower} Kg,', end=' ')
print(f'from {lighter}')
