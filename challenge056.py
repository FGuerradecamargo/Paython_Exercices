average_age = []
men = []
women_under = 0
name_man = ''
for p in range(1, 5):
    print('{:-^20}'.format(f' {p} PERSON '))
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    sex = str(input('Sex [M/F]: ')).strip().upper()
    average_age.append(age)
    if sex in 'Mm':
        men.append(age)
    if sex in 'Ff' and age < 20:
        women_under = women_under + 1
    if sex == 'M':
        name_man = name
        if age > age:
            name_man = name

print(f'The average age is {(sum(average_age)) / p}')
print(f'The older man is {max(men)} years old and he is called {name_man}')
print(f'We have {women_under} women under 20 years old')