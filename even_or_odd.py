from random import randint
from time import sleep

print('-' * 30)
print('Lets play even or odd')
print('-' * 30)

counter = 0

while True:
    player = str(input('Even or Odd? [E/O]: ')).strip().upper()[0]
    player1 = int(input('Enter your number: '))
    computer = randint(0, 5)
    total = player1 + computer
    print('-' * 30)
    c1 = ''

    if total % 2 == 0:
        c1 = 'Even'
    elif total % 2 != 0:
        c1 = 'Odd'

    print(f'You chose {player1} and the computer {computer}')
    sleep(0.8)
    print(f'{total} is {c1}')
    sleep(0.8)
    if player == 'E' and c1 == 'Even' or player == 'O' and c1 == 'Odd':
        counter += 1
        print('\033[1;31mYou won! Lets play again.\033[m')
    else:
        print('\033[1;31mYou lost')
        break

print(f'You won {counter} times.')
