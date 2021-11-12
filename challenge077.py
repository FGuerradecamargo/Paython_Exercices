words = ('learn', 'program', 'language', 'python', 'course', 'free', 'study', 'practice',
         'work', 'market', 'programmer', 'future')

for p in words:
    print(f'\nIn the word: \033[1;31m{p}\033[m we have ', end='')
    for letter in p:
        if letter.lower() in 'aeiou':
            print(f'\033[1;31m{letter}\033[m', end='')

