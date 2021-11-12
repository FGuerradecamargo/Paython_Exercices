t = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
     'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
     'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
     while True:
          n = int(input('Enter a number between 0 and 20: '))
          if 0 <= n <= 20:
               break
          print('Invalid number!', end='')
     print('You have entered the number', t[n])
     q = str(input('Do you wish to continue? [Y/N]: ')).strip().upper()[0]
     print('=' * 35)
     while q not in 'NY':
          q = str(input('Invalid answer! Do you wish to continue? [Y/N]: ')).strip().upper()[0]
          if q == 'N':
               break
     if q == 'N':
          break
print('Program finished!')