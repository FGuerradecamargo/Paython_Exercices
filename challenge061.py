print('=' * 20)
print('{:^20}'.format('10 TERM OF A PA'))
print('=' * 20)

first_term = int(input('Enter the first term: '))
reason = int(input('Enter the reason: '))
pi = first_term
counter = 0

while counter < 10:
    pi = pi + reason
    counter += 1
    print(pi, end=' > ')

print('END')