print('{:=^48}'.format('MULTIPLICATION TABLE'))
number = int(input('Enter a number to see its multiplication table: '))

for c in range(1, 11):
    print('{} x {} = {}'.format(number, c, number * c))