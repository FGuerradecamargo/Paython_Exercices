print('=' * 35)
print('{:^35}'.format('IRELAND STORE'))

total_price = []
over100 = counter = lower_price = 0
cheaper = ' '

while True:
    print('=' * 35)
    product = str(input('Product: ')).strip().upper()
    price = float(input('Price: £ '))
    counter += 1
    total_price.append(price)
    if price > 1000:
        over100 += 1
    if counter == 1:
        cheaper = product
        lower_price = price
    else:
        if price < lower_price:
            cheaper = product
            lower_price = price
    q = ' '
    while q not in 'NY':
        q = str(input('Do you wish to continue? [Y/N]: ')).strip().upper()[0]
    if q == 'N':
        break
print('=' * 35)

print(f'The total spent is: {sum(total_price):.2f}')
print(f'{over100:.2f} products have cost more than £ 100.00')
print(f'The cheaper product is {cheaper} and it have cost {lower_price:.2f}')