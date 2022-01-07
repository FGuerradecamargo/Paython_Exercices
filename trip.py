# ask the distance, calculate the price (0,50 km up to 200 km, after 200 km 0,45)
distance = float(input('Enter the distance in km: '))
short = 0.50
long = 0.45

if distance > 200:
    print('The price for the trip will be: £ {:.2f}'.format(distance * long))
else:
    print('The price for the trip will be: £ {:.2f}'.format(distance * short))

