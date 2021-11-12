from random import randint
from time import sleep
numbers = []


def draw(list):
    for c in range(0, 5):
        list.append(randint(0, 10))


def sum_even(list):
    even = []
    for e in numbers:
        if e % 2 == 0:
            even.append(e)
    print(sum(even))


draw(numbers)
print(f'Drawing 5 number:', end=' ')
sleep(1)
for n in numbers:
    print(n, end=' ')
    sleep(1)
print('Ready!')
sleep(1)
print(f'Summing the even numbers in {numbers}, we have', end=' ')
sleep(1)
sum_even(list)
