grade1 = float(input('Enter the first grade: '))
grade2 = float(input('Enter the second grade: '))
average = (grade1 + grade2) / 2

if average > 5.0 and average <= 6.9:
    print('Your average grade is {}. \033[1;31mYou are under recuperation!\033[m'.format(average))
elif grade1 > 10 or grade2 > 10:
    print('Invalid grade. Try again!')
elif average >= 7.0:
    print('Your average grade is {}. \033[1;31mYou are approved. Congratulations!!!\033[m'.format(average))
else:
    print('Your average grade is {}, \033[1;31mYou are failed. You should study more!\033[m'.format(average))
