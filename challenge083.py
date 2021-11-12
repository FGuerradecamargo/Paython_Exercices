opened = []
closed = []
expression = str(input('Enter an expression: ')).strip()
for a in expression:
    if a in '(':
        opened.append(a)
    elif a in ')':
        closed.append(a)
if len(opened) == 0 and len(closed) == 0:
    print('You did not use parentheses!')
elif len(opened) == len(closed):
    print('Your expression is right!')
else:
    print('Your expression is wrong! Correct it.')