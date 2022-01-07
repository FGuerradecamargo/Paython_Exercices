sum = 0
count = 0

for c in range(1, 7):
    n = int(input('Enter the {} number: '.format(c)))
    if n % 2 == 0:
        sum += n
        count = count + 1

print('The sum of all {} odd numbers is: {}'.format(count, sum))


