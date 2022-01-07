print('=-=' * 15)
print('TRIANGLE ANALYSER')
print('=-=' * 15)

l1 = float(input('Enter the first line: '))
l2 = float(input('Enter the second line: '))
l3 = float(input('Enter the third line: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Yes, those numbers can form a triangle!')
    if l1 == l2 and l1 == l3:
        print('The triangle is \033[1;32mEquilateral!')
    elif l1 == l2 and l1 != l3 or l2 == l3 and l2 != l1 or l3 == l1 and l3 != l2:
        print('The triangle is \033[1;32mIsosceles!')
    else:
        print('The triangle is \033[1;32mscalene!')

else:
    print('No, those numbers cannot form a triangle!')
