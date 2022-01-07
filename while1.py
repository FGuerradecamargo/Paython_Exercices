sum = counter = 0

while True:
    n = int(input('Enter a number: '))
    if n == 999:
        break
    counter += 1
    sum += n

print('-' * 60)
print(f'{counter} numbers have been entered and the sum between them is {sum}')
print('-' * 60)
