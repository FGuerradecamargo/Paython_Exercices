def record(n='Unknown', g=0):
    name = str(input('Name: '))
    goal = str(input('How many goals did he scored? '))
    if name != '':
        n = name
    if goal != '' and goal.isnumeric():
        g = int(goal)
    print(f'The player {n} scored {g} times')


record()
