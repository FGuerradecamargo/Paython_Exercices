list = []
n1 = 0
max = min = 0
counter = 0
for c in range(0, 5):
    n = int(input('Enter a number: '))
    if c == 0:
        max = min = n
        print('first...')
        list.append(n)
    else:
        if n >= max:
            max = n
            list.insert(5, n)
            print('Added at the end of the list...')
        elif n <= min:
            min = n
            list.insert(0, n)
            print('Added at the position 0 of the list...')
        elif min <= n <= max:
            print('Added at the position 1 of the list...')
            list.insert(1,n)
            n1 = n
print('-=' * 30)
print(f'The numbers enter are: {list}')