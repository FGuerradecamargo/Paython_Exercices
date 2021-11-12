list = []
grade = []
temporary = []
student = []
ask2 = 0

while True:
    name = str(input('Name: ')).strip().upper()
    grade1 = float(input('Grade 1: '))
    grade2 = float(input('Grade 2: '))
    average = (grade1 + grade2) / 2
    list.append([name, [grade1, grade2], average])
    ask = ' '
    while ask not in 'NY':
        ask = str(input('Do you wish to continue? [Y/N]: ')).strip().upper()
    if ask in 'N':
        break
print('-=' * 40)

print(f'{"Nu.":<4}{"Name":<18}{"Average":>8}')
print('-=' * 40)
for c, v in enumerate(list):
    print(f'{c:<3}', end=' ')
    print('{:<20}'.format(v[0]), end=' ')
    average = sum(list[c][1]) / 2
    print(average)
print('-=' * 40)

while True:
    ask2 = int(input('Which student do you wish to see the grades from? \033[1;31m(999 to close): \033[m'))
    if ask2 != 999:
        print(f"{list[ask2][0]}'s grades: {list[ask2][1]}")
    if ask2 == 999:
        break
print('-=' * 40)
print('Program closed!')
