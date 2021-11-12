from random import randint
from time import sleep
print('=' * 40)
print('{:^38}'.format('EURO MILLION'))
print('=' * 40)
games = []
temporary = []
ask = int(input('How many games do you wish to play? '))
for c in range(0, ask):
    while len(temporary) < 6:
        n = (randint(1, 60))
        if n not in temporary:
            temporary.append(n)
    games.append(temporary[:])
    temporary.clear()
    print(f'{c + 1}º game: {sorted(games[c])}')
print('{:-^40}'.format(' < Good luck! > '))