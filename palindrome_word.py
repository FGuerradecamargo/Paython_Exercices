phrase = str(input('Enter a phrase: ')).strip().upper()

words = phrase.split()
j = ''.join(words)
inverted = j[::-1]

print(f'{phrase} inverted is: {inverted}')
if j == inverted:
    print(f'\033[1;31m{phrase} is a Palindrome!')
else:
    print(f'\033[1;31m{phrase} is not a Palindrome!')
