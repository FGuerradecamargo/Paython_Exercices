number = 0
counter = 0
numbers = []

number = int(input('Enter a number (or 999 to stop): '))
while number != 999:
    if number != 999:
        numbers.append(number)
    counter += 1
    # s += n
    number = int(input('Enter a number (or 999 to stop): '))
print(f'You have entered {counter} number and them sum of them numbers is: {sum(numbers)}.')
# print(s - 999)
