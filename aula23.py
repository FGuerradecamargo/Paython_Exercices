def factorial(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


num = int(input('Enter a number: '))
fat = factorial(num)
print(f'The factorial of {num} is {fat}')
