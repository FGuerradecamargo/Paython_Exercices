player = {}
goals = []
players_list = []

while True:
    player['name'] = str(input('Name: ')).strip()
    games = int(input(f'How many games did {player["name"]} played? '))
    for c in range(1, games + 1):
        goals.append(int(input(f'   How many goals in the game {c}: ')))
    player['goals'] = goals[:]
    player['total'] = sum(goals)
    players_list.append(player.copy())
    goals.clear()
    question = ' '
    while question not in 'YN':
        question = str(input('Do you wish to continue? [Y/N]: ')).strip().upper()[0]
        if question in 'NY':
            break
    if question in 'N':
        break
print('-=' * 35)
print('Cod  name       goals        total')
print('-' * 35)
for c, v in enumerate(players_list):
    print(f'{c:<3}  {v["name"]:<10} {v["goals"]} {v["total"]:>10}')
print('-' * 35)
while True:
    question2 = int(input('Show which player s dados? [999 to close]: '))
    if question2 != 999:
        print(f'{players_list[question2]["name"]} s dates:')
        for c, v in enumerate(players_list[question2]['goals']):
            print(f'- In the {c + 1}º match he scored {v} times')
        print('-' * 35)
    if question2 == 999:
        break
print('<<< Program Closed >>>')
