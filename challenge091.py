from random import randint
from time import sleep
from operator import itemgetter
games = {}
for n in range(1, 5):
    games[f'{n}'] = randint(1, 6)
print('Values drawn: ')
for k, v in games.items():
    sleep(0.7)
    print(f'The player {k} got {v}')
sleep(0.7)
ranking = sorted(games.items(), key=itemgetter(1), reverse=True)
print('-=' * 17)
print(f'    == Ranking of players ==')
for i, v in enumerate(ranking):
    sleep(0.7)
    print(f"  {i + 1}º position: player {v[0]} with {v[1]}")
