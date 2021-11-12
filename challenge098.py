def counter(s, e, i):
    from time import sleep
    if i == 0:
        print('Error! O in not an option!')
    if i < 0:
        i *= -1
        print(f'The count from {s} to {e} in {i} to {i} is:')
        i *= -1
        sleep(1)
        for c in range(s, e - 1, i):
            print(c, end=' ')
            sleep(0.5)
    if i > 0:
        print(f'The count from {s} to {e} in {i} to {i} is:')
        sleep(1)
        for c in range(s, e + 1, i):
            print(c, end=' ')
            sleep(0.5)
    print('END!')
    sleep(1)
    print('-=' * 20)


counter(1, 10, 1)
counter(10, 0, -2)
print('Now it is your turn!')
s = int(input('Start: '))
e = int(input(('End: ')))
i = int(input('Range: '))
counter(s, e, i)