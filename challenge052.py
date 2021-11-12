n = int(input('Enter a number to know if its prime: '))
count = 0

for c in range(1, n + 1):
    if n % c == 0:
        count = count + 1

if count == 2:
    print(f'The number {n} was divided {count} time.\n\033[1;31mThe number is prime!')
else:
    print('The number {} was divided {} time.\n\033[1;31mThe number is not prime!'.format(n, count))
