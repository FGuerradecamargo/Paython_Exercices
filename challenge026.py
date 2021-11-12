f = str(input('Enter a phrase: ')).strip().lower()

print('The letter A appears: {}'.format(f.count('a')))
print('The letter A appears for the first time in the position: {}'.format(f.find('a')))
print('The letter A appears for the last time in the position: {}'.format(f.rfind('a')))
