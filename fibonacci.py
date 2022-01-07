print('-' * 40)
print('{:^40}'.format('Fibonacci sequence'))
print('-' * 40)

n = int(input('How many terms do you want to see? '))
counter = 0
f1 = 0
f2 = 1
f_n = 0

print('-' * 40)

while counter < n:
    print(f_n, end=' > ')
    f_n = f1 + f2
    f2 = f1
    f1 = f_n

    counter += 1
print('End')
