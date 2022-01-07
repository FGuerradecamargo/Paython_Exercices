from random import randint

list = []
t = tuple()
r = 0
counter = 0

while True:
    r = randint(0, 10)
    counter += 1
    list.append(r)
    if counter == 5:
        break

t1 = (tuple(list) + t)

print(f'The random numbers are: {t1}')
print(f'The higher is: {max(t1)}')
print(f'The lower is: {min(t1)}')
