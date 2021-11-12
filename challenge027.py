n = str(input('Enter your full name: ')).strip().capitalize()
s = n.split()

print('your first name is: {}'.format(s[0].capitalize()))
print('Your last name is: {}'.format(s[len(s) -1].capitalize()))
