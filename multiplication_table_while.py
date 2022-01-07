while True:
    print('-' * 60)
    n = int(input('What number do you want to see the multiplication table?  (-1 to close): '))
    print('-' * 60)
    if n < 0:
        break
    for t in range(1, 11):
        print(t, 'x', n, '=', t * n)

print('Program finished. Check back often. ')
