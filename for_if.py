from datetime import date

today = date.today().year
over = 0
under = 0

for e in range(1, 8):
    n = int(input(f'Enter the {e} year of birth: '))
    if today - n >= 21:
        over = over + 1
    else:
        under = under + 1

print(f'We have {over} people over 21.')
print(f'We have {under} people under 21.')