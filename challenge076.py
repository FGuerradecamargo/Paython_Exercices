print('=' * 37)
print('PRICE LIST')
print('=' * 37)

list = ('bread', 3.50, 'milk', '1', 'chicken', 10.90)
for pos in range(0, len(list)):
    if pos % 2 == 0:
        print(f'{list[pos]:.<30}', end='')
    else:
        print(f'£{list[pos]:>5}')
print('=' * 37)