list = []
higher = lower = 0

for c in range(0, 5):
    list.append(int(input(f'Enter a number for the position {c}: ')))

print('=' * 60)
print(f'You have entered the numbers: {list}')
print(f'The higher number in the list is: {max(list)} and its in the potion ', end='')
for i, v in enumerate(list):
    if v == max(list):
        print(f'{i}...', end='')
print(f'\nThe lower number in the list is: {min(list)} and its in the position ', end='')
for i, v in enumerate(list):
    if v == min(list):
        print(f'{i}... ', end='')
print()