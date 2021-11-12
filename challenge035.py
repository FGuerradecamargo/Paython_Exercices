# ask for the three lines, show if they can or cannot form an angle
# the sum of 2 sides must be bigger than the third one
print('=-=' * 15)
print('TRIANGLE ANALISER')
print('=-=' * 15)

l1 = float(input('Enter the first line: '))
l2 = float(input('Enter the second line: '))
l3 = float(input('Enter the third line: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Yes, those numbers can form a triangle!')
else:
    print('No, those numbers cannot form a triangle!')
