def read_int(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERROR! Enter a whole number!\033[m')
        except KeyboardInterrupt:
            print('\033[31mUser decided not to enter the whole number!\033[m')
            return 0
        else:
            return num


def read_float(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERROR! Enter a real number!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUser decided not to enter the real number!\033[m')
            return 0
        else:
            return num


print('=' * 30)
n = read_int('Enter a whole number: ')
f = read_float('Enter a real number: ')
print('=' * 30)
print(f'The whole number entered was {n} and the real number was {f}')
