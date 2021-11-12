from random import randint
from time import sleep
print('{:=^35}'.format('JOKEMPO'))

print('''OPTIONS:
[0] Stone
[1] Paper
[2] Scissor''')
print('=-=' * 15)
stone = 'Stone'
paper = 'Paper'
scissor = 'Scissor'

user_option = int(input('Enter your option: '))
print('=-=' *15)
pc_option = randint(0, 2)
list = ('Stone', 'Paper', 'Scissor')
print('your option: {}'.format(list[user_option]))
sleep(1)
print('PC option: {}'.format(list[pc_option]))
sleep(1)

if user_option == 0 and pc_option == 0:
    print('\033[1;31mEven!')
    sleep(1)
    print('TRY AGAIN!')
elif user_option == 0 and pc_option == 1:
    print('\033[1;31m{} wins {}. You lost.'.format(paper, stone))
    sleep(1)
    print('TRY AGAIN!')
elif user_option == 0 and pc_option == 2:
    print('\033[1;31m{} wins {}.'.format(stone, scissor))
    sleep(1)
    print('YOU WON. CONGRATULATIONS!!!')
elif user_option == 1 and pc_option == 0:
    print('\033[1;31m{} wins {}.'.format(paper, stone))
    sleep(1)
    print('YOU WON. CONGRATULATIONS!!!')
elif user_option == 1 and pc_option == 1:
    print('\033[1;31mEven.')
    sleep(1)
    print('Try again!')
elif user_option == 1 and pc_option == 2:
    print('\033[1;31m{} wins {}. You lost!'.format(scissor, paper))
    sleep(1)
    print('Try again!')
elif user_option == 2 and pc_option == 0:
    print('\033[1;31m{} win {}. You lost!'.format(stone, scissor))
    sleep(1)
    print('Try again!')
elif user_option == 2 and pc_option == 1:
    print('\033[1;31m{} wins {}.'.format(scissor, paper))
    sleep(1)
    print('You won! Congratulations!!!')
elif user_option == 2 and pc_option == 2:
    print('\033[1;31mEven.')
    sleep(1)
    print('TRY AGAIN!')
else:
    print('\033[1;31mInvalid option!')
