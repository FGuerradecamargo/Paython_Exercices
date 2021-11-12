guy = list()
date = list()
higher = smaller = 0
for c in range(0,3):
    date.append(str(input('Name: ')))
    date.append((int(input('Age: '))))
    guy.append(date[:])
    date.clear()

for p in guy:
    if p[1] > 21:
        print(f'{p[0]} is over 18.')
        higher +=1
    else:
        print(f'{p[0]} is under age')
        smaller += 1
print(f'There are {higher} over 18 and {smaller} under age!')
