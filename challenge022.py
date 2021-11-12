name = str(input('Enter your full name: ')).strip()
# name with all the capital letters
print('Your name in capital letters is: ', name.upper())
# name with all lower case letter
print('Your name in lower case letters is: ', name.lower())
# how many letter has the name without consider spaces
print('Your full name has: {} letters!'.format(len(name) - name.count(' ')))
# fist name and how many letters it has
s = name.split()
print('Your first name is: {} and it has: {} letters!'.format(s[0], len(s[0])))
#and it has {} letters!