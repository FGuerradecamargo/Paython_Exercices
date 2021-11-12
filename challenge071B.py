print('Bank notes available: £50, £20, £10, £1')
v = int(input('How mach do you wish to withdraw? £ '))
print('=' * 35)
banknote = 50
total = v
counter = 0

while True:
    if total >= banknote:
        total -= banknote
        counter += 1
    else:
        if counter > 0:
            print(f'{counter} of {banknote}')
        if banknote == 50:
            banknote = 20
        elif banknote == 20:
            banknote = 10
        elif banknote == 10:
            banknote = 1
        counter = 0
        if total == 0:
            break