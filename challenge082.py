list = []
even_lis = []
odd_list = []
while True:
    list.append(int(input('Enter a number: ')))
    ask = ' '
    while ask not in 'YyNn':
        ask = str(input('Do you wish to continue? {Y/N]: ')).strip()[0]
    if ask in 'Nn':
        break
print('=' * 40)
print(f'The complete list is: {list}')
for n in list:
    if n % 2 == 0:
        even_lis.append(n)
    else:
        odd_list.append(n)
print(f'The list of even numbers is: {even_lis}')
print(f'The list of odd numbers is: {odd_list}')
