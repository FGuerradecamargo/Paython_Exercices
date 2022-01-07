print('=' * 20)
print('{:^20}'.format('10 TERM OF A PA'))
print('=' * 20)

b = int(input('Enter the first term: '))
r = int(input('Enter the reason: '))
tenth = b + (10 - 1) * r

for c in range(b, tenth + r, r):
    print(c, end=' > ')

print('END')
