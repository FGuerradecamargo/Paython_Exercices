person = {}
people = []
counter = total_age = 0
while True:
    person['name'] = str(input('Name: ')).strip()
    counter += 1
    while True:
        person['sex'] = str(input('Sex [M/F]: ')).strip().upper()[0]
        if person['sex'] in 'MF':
            break
        print('Error! enter M or F!')
    person['age'] = int(input('Age: '))
    total_age += person['age']
    people.append(person.copy())
    question = ' '
    while question not in 'YN':
        question = str(input('Do you wish to continue? [Y/N]: ')).strip().upper()[0]
    if question in 'N':
        break
print('-=' * 35)
print(f'- {counter} people was entered')
print(f'- The average age is {total_age / counter:.2f}')
print(f'- The women in the list are:', end=' ')
for c in range(0, len(people)):
    if people[c]['sex'] in 'F':
        print(people[c]['name'], end=' ')
print()
print('- List of people over average age:')
for c in range(0, len(people)):
    if people[c]['age'] > total_age / counter:
        for k, v in people[c].items():
            print(f"   {k} = {v};", end=' ')
        print()
print('<<< PROGRAM FINISHED >>>')
