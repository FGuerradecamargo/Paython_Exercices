import random
a1 = str(input('Enter the first name: '))
a2 = str(input('Second name: '))
a3 = str(input('third name: '))
a4 = str(input('forth name: '))
list = [a1, a2, a3, a4]
random.shuffle(list)
print('The order of presentation will be: ')
print(list)
