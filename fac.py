from challenge102 import factorial
fac21 = factorial(21)
fac5 = factorial(5)
fac2 = factorial(2)
fac7 = factorial(7)
fac9 = factorial(9)

question_a = fac21 / (fac5 * (factorial(21 - 5)))
print(f'with 21 characters we can do {question_a:.0f} groups of 5')
prob_def = fac7 / (fac2 * (factorial(7 - 2)))
prob_ata = fac9 / (fac2 * (factorial(9 - 2)))
prob_cur = fac5 / (1 * (factorial(5 - 1)))
question_b = prob_def * prob_cur * prob_ata
print(f'The combination possibles are: {question_b:.0f}')
