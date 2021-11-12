n = 0
counter = 0
list = []
#s = 0 resolucao sem a lista

n = int(input('Enter a number (or 999 to stop): '))
while n != 999:
    if n != 999:
        list.append(n)
    counter += 1
    # s += n
    n = int(input('Enter a number (or 999 to stop): '))
print(f'You have entered {counter} number and them sum of them numbers is: {sum(list)}.')
#print(s - 999)
