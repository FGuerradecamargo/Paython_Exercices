from datetime import date
# ask the year, calculate if it's leap year or not
year = int(input('Enter a year or number 0 to analise the current year: '))

if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('{} is a leap year!'.format(year))

else:
    print('{} is not a leap year!'.format(year))
