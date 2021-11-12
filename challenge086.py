p1 = p2 = 0
matrice = [[], [], [], [], [], [], [], [], []]
for c in range(0, 9):
    n = int(input(f'Enter the number for [{p1},{p2}]: '))
    matrice[c].append(n)
    p2 += 1
    if c == 2:
        p1 = 1
        p2 = 0
    if c == 5:
        p1 = 2
        p2 = 0
print('=' * 47)
print(f'{matrice[0]}  {matrice[1]}  {matrice[2]}')
print(f'{matrice[3]}  {matrice[4]}  {matrice[5]}')
print(f'{matrice[6]}  {matrice[7]}  {matrice[8]}')

'''matrice = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range (0, 3):
        matrice[l][c] = int(input(f'Enter a number for [{l},{c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrice[l][c]:^5}]', end='')
    print()'''