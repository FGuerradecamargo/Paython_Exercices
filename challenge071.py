print('=' * 35)
print('{:^35}'.format('IRELAND BANK'))
print('=' * 35)

r1 = r2 = r3 = r4 = 0

print('Bank notes available: £50, £20, £10, £1')
v = int(input('How mach do you wish to withdraw? £ '))
print('=' * 35)


r1 = v % 50
if v // 50 != 0:
    print(v // 50, 'banknotes of £50')
if v % 50 != 0:
    r2 = r1 % 20
    if r1 // 20 != 0:
        print(r1 // 20, 'banknotes of £20')
    if r1 % 20 != 0:
        r3 = r2 % 10
        if r2 // 10 != 0:
            print(r2 // 10, 'banknotes of 10')
        if r3 % 10 != 0:
            r4 = r3 % 1
            print(r3 // 1, 'banknotes of 1')

print('=' * 35)
total = (r3 // 1 * 1) + (r2 // 10 * 10) + (r1 // 20 * 20) + (v // 50 * 50)
print(f'You withdrew £{total:.2f}! Have a good day.')
