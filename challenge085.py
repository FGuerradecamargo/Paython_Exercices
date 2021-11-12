list = [[], []]
for r in range(1, 8):
    n = int(input(f'Enter the {r}º number: '))
    if n % 2 == 0:
        list[0].append(n)
    else:
        list[1].append(n)
print('=' * 47)
print(f'The even numbers entered are: {sorted(list[0])}')
print(f'The odd numbers entered are: {sorted(list[1])}')

