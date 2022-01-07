# ask wage, calculate the increase (up to 1250 + 15%, more than 1250 + 10%)

wage = float(input('Enter the current wage: £ '))

if wage > 1250:
    print('Your new wage is: £ {:.2f}'.format(wage * (10/100) + wage))
else:
    print('Your new wage is: £ {:.2f}'.format(wage * (15/100) + wage))
