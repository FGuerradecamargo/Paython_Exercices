import random


a1 = str(input('Enter the fist student: '))
a2 = str(input('Enter the second student: '))
a3 = str(input('Enter the third student: '))
a4 = str(input('Enter the forth student: '))
list = [a1, a2, a3, a4]
s = random.choice(list)
print('The student chosen is: {}'.format(s))
