from random import randint
from time import sleep


na = int(randint(1, 5))

print('=-=' * 12)
print('LETS START THE GAME!!!')
print('=-=' * 12)
nchosen = int(input('Chose a number between 1 and 5: '))

print('Loading...')
sleep(0.8)



if na == nchosen:

    print('The number is: {}'.format(na))
    sleep(0.8)
    print('You win!!! CONGRATULATIONS !!! ')


else:
    print('The number is: {}'.format(na))
    sleep(0.8)
    print('You lost. Give it another try. ')

print('=-=' * 12)
