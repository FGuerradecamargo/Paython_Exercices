sex = str(input('Enter your sex [M/F]: ')).strip().upper()[0]
while sex not in 'MmFf':
    sex = str(input('Invalid answer. Please enter your sex [M/F]: ')).strip().upper()[0]

print(f'Sex {sex} was registered successfully.')