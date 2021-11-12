def factorial(num, show=False):
    """
    => Calculates the factorial of a number.
    :param num: Number to be calculated
    :param show: (optional), show or not the calculation
    :return: return the factorial of num
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return f


#print(factorial(4, False))
#print(factorial(4, True))
