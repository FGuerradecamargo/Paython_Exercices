from time import sleep
print('\033[1;31m{:=^20}'.format('COUNTDOWN'))
countdown = int(input('\033[mEnter 1 to start: '))

if countdown == 1:
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    print('\033[1;31m{:^25}'.format('BOM!!! BOM!!! BOM!!!'))
