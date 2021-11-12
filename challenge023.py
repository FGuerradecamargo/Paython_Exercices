n = int(input('Enter a number between 0 and 999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Unity: {}'.format(u))
print('ten: {}'.format(d))
print('hundred: {}'.format(c))
print('Thousand: {}'.format(m))
