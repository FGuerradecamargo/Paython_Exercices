over18 = []
men = []
women_under18 = []

while True:
    print('-' * 35)
    print('{:^34}'.format('REGISTER A PERSON'))
    print('-' * 35)

    while True:
        age = int(input('Age: '))
        if age < 120:
            break
        if age > 18:
            over18.append(age)
    sex = ' '
    while sex not in 'FM':
        sex = str(input('Sex [F/M]: ')).strip().upper()[0]
    if sex == 'M':
        men.append(sex)
    if sex == 'F'and age < 20:
        women_under18.append(age)
    q = ' '
    while q not in 'YN':
        q = str(input('Do you wish to continue? [Y/N]: ')).strip().upper()[0]
    if q == 'N':
        break

print('Program finished.')
print('-' * 35)
print(f'{len(over18)} people are over 18\n{len(men)} are men\n{len(women_under18)} are women under 20')
print('-' * 35)