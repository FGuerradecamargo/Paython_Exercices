n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
option = 0
while option != 5:
    print('=-=' * 13)
    print('''Choose one of the option:
    [1] Sum 
    [2] Multiply
    [3] Bigger
    [4] Enter new numbers
    [5] Close the program''')

    option = int(input('Enter your option: '))
    if option == 1:
        print(f' {n1} + {n2} = ', n1 + n2)
    elif option == 2:
        print(f'{n1} x {n2}  = ', n1 * n2)
    elif option == 3:
        print(f'The bigger number between {n1} and {n2} is: ', max(n1, n2))
    elif option == 4:
        n1 = int(input('Enter the first number: '))
        n2 = int(input('Enter the second number: '))
    elif option > 5:
        print("invalid option!")

print('Program closed.')