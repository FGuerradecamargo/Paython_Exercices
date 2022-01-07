print('=-=' * 5, 'IMC Calculator', '=-=' * 5)
weight = float(input('Enter your weight (kg): '))
height = float(input("Enter your height (mt): "))

imc = weight / (height ** 2)

if imc < 18.5:
    print('Your imc is: {:.2f}, you are under weight!'.format(imc))
elif imc <= 25:
    print('Your imc is: {:.2f}, you are at your ideal weight! Congratulations!!!'.format(imc))
elif imc <= 30:
    print('Your imc is: {:.2f}, you are overweight!'.format(imc))
elif imc <= 40:
    print('Your imc is: {:.2f}, you have obesity!'.format(imc))
else:
    print('Your imc is: {:.2f}, you have morbid obesity!'.format(imc))
