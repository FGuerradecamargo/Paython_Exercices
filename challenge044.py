print('{:=^35}'.format('IRELAND SHOP'))

price = float(input('Enter the price of the product: '))
print('''Payment Methods:
[1] Cash: money or check
[2] By card: 1x
[3] By card: 2x 
[4] By card: 3x or more''')
pyment_method = int(input('Enter the payment method: '))

cash = price - (price * (10 / 100))
card1 = price - (price * (5 / 100))
card2 = price
card3 = price * (20 / 100) + price

if pyment_method == 1:
    print('The price is £{:.2f} with 10% discount.'.format(cash))
elif pyment_method == 2:
    print('The price is : £{:.2f}, with 5% discount.'.format(card1))
elif pyment_method == 3:
    print('The price is: £{:.2f}, It is normal price.'.format(card2))
elif pyment_method == 4:
    print('The price is: £{:.2f}, increased 20%.'.format(card3))
    installment = int(input('Enter the number of installment: '))
    print('You will pay {} x {:.2f}.'.format(installment, card3 / installment))
else:
    print('\033[1;31mInvalid option!')