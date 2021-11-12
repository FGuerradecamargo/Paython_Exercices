from datetime import date
birth = int(input('Enter your year of birth: '))
date = date.today().year
age = date - birth

if age <= 9:
    print('Your are {} years old,\nYour category is \033[1;32mMirim!\033[m'.format(age))
elif age <= 14:
    print('You are {} years old,\nYour category is \033[1;32mInfantil!\033[m'.format(age))
elif age <= 19:
    print('You are {} years old,\nYour category is \033[1;32mJunior!\033[m'.format(age))
elif age == 25:
    print('You are {} years old,\nYour category is \033[1;32mSenior!\033[m'.format(age))
else:
    print('You are {} years old,\nYour category is \033[1;32mMaster!\033[m'.format(age))

