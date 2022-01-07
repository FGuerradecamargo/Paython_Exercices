print('=' * 20)
print('{:^20}'.format('10 TERM OF A PA'))
print('=' * 20)

first_term = int(input('Enter the first term: '))
reason = int(input('Enter the reason: '))
counter = 1
total = 10
more = 1

while more != 0:
    total = total + more
    while counter < total:
        print(first_term, end=' > ')
        first_term += reason
        counter += 1
    print('PAUSE')
    more = int(input('How many more terms do you want?'))
print('END!')
