def read_int(msg):
    ok = False
    while ok == False:
        num = input(msg)
        if num.isnumeric():
            ok = True
            return num
        else:
            print('\033[1;31mERROR! Enter a whole number!\033[m')


print('=' * 30)
n = read_int('Enter a number: ')
print(f'You have entered the number {n}')
