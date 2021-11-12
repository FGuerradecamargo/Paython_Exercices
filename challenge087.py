even_number = []
matrices = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range (0, 3):
        matrices[l][c] = int(input(f'Enter a number for [{l},{c}]: '))
print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrices[l][c]:^5}]', end='')
    print()

for e in matrices:
    for even in e:
        if even % 2 == 0:
            even_number.append(even)

print('-=' * 30)
print(f'The sum of the even numbers is: {sum(even_number)}')
s = matrices[0][2], matrices[1][2], matrices[2][2]
print(f'The sum of the numbers in the third column is: {sum(s)}')
print(f'The higher number in the second line is: {max(matrices[1])}')