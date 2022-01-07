from random import randint
from time import sleep

random_number = int(randint(1, 5))

print('=-=' * 12)
print('LETS START THE GAME!!!')
print('=-=' * 12)
user_number = int(input('Chose a number between 1 and 5: '))

print('Loading...')
sleep(0.8)

if random_number == user_number:
    print(f'The number is: {random_number}')
    sleep(0.8)
    print('You win!!! CONGRATULATIONS !!! ')
else:
    print('The number is: {}'.format(random_number))
    sleep(0.8)
    print('You lost. Give it another try. ')

print('=-=' * 12)
