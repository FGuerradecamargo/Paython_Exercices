import math
a = float(input('Enter an angle: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('The angle {} has sine {:.2f}, the cosine {:.2n} and tangent {:.2f} '.format(a, s, c, t))

