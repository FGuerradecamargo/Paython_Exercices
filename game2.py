from random import randint
from time import sleep

print('=-=' * 12)
print('I am your computer...\nJust thought a number between 1 and 10\nWould like to guess it?')
print('=-=' * 12)

random_number = int(randint(0, 10))
player_number = int(input('Choose a number between 0 and 10: '))
counter = 1

while player_number != random_number:
    counter += 1
    if player_number > random_number:
        print('A little lower...')
    else:
        print('A little higher...')
    player_number = int(input('Give it another try: '))


print('That is right!')
sleep(0.8)
print(f'You needed {counter} attempts to get it right.')
sleep(0.8)
print('=-=' * 12)
