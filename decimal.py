n = int(input('Enter a number between 0 and 999: '))
unt = n // 1 % 10
dez = n // 10 % 10
cent = n // 100 % 10
mil = n // 1000 % 10

print('Unity: {}'.format(unt))
print('ten: {}'.format(dez))
print('hundred: {}'.format(cent))
print('Thousand: {}'.format(mil))
