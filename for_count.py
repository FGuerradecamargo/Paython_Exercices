sum = 0
count = 0

for c in range(1, 500, 2):
   if c % 3 == 0:
       count += 1
       sum = sum + c

print('The sum of all {} numbers is: {}'.format(count, sum))
