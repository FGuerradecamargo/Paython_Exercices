# ask the car speed, compare with the limit allowed (80), show the massage (charge = 7 per km)
speed = float(input('Enter the speed: '))
allowed = 80
charge = (speed - allowed) * 7

if speed > allowed:
    print('You have exceeded the speed limit of {} km/h!\n You will be charged in £ {:.2f}.'.format(allowed, charge))

else:
    print('You are within the speed limit.')
    print('Have a nice day! Drive SAFELY!')