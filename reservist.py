from datetime import date
# ask the day of birth, according to the age inform the reservist status
# still to go, up to go or late

birth = int(input('Enter your year of birth: '))
sex = str(input('Are you male or female? '))
hj = date.today().year
age = hj - birth

if sex == 'female':
    print('You are a female, you do not have to enlist.')
elif age == 18:
    print('You are {} years old, you have to enlist immediately!'.format(age))
elif age > 18:
    print('You are {} years old, you are {} years late!.'.format(age, age - 18))
else:
    print('You are {} years old, you are {} years under age, Wait until {}'.format(age, 18 - age, birth + 18))


