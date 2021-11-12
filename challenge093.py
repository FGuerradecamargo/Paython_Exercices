player = {}
goals = []
player['name'] = str(input('Name: ')).strip()
games = int(input(f'How many games did {player["name"]} played? '))
for c in range(1, games + 1):
    goals.append(int(input(f'   How many goals in the game {c}: ')))
player['goals'] = goals[:]
player['total'] = sum(goals)
print('-=' * 25)
for k, v in player.items():
    print(f'{k} has the value {v}')
print('-=' * 25)
print(f'The player {player["name"]} played in {games} matches:')
for c in range(0, games):
    print(f'  => in the game {c + 1}, {player["name"]} has scored {goals[c]} times')
print(f'{sum(goals)} goals in total')
