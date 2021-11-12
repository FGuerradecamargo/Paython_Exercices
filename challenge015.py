kmr = float(input('How many kilometers? '))
d = int(input('How many days? '))
# 60 per day + 0,15 per km
t = (kmr * 0.15) + (d * 60)
print('The total is: £ {:.2f}'.format(t))

