import math
ca = float(input('Enter the adjacent side: '))
co = float(input('Enter the opposite sie: '))
h = math.hypot(ca, co)
'''h = (ca ** 2 + co ** 2) ** (1/2)'''
print('The hypotenuse is: {:.2f}'.format(h))




