# ask the value of the house, the wage of the buyer and how many year to pay
# calculete the monthly installment (cannot be more tha 30% of the wage)
print('=-=' * 5, '\033[1;31mLOAN CALCULATOR\033[m', '=-=' * 5)
h = float(input('enter the price of the house: £ '))
wage = float(input('Enter your monthly wage: £ '))
t = int(input('Enter the number of the years for payment: '))
installment = h / (t * 12)

if installment > (wage * (30/100)):
       print('Your loan was \033[1;34mdined!\033[m The installment cannot be more than 30% of your monthly wage.')
       print('The monthly installment is: £ \033[1;31m{:.2f}\033[m\nYour maximum monthly payment is: £ \033[1;31m{:.2f}\033[m'.format(installment, (wage * (30/100))))
else:
       print('\033[1;34mCONGRATULATIONS!!! Your loan is approved.\033[m')
       print('Your monthly installment will be: £ \033[1;31m{:.2f}\033[m'.format(installment))

