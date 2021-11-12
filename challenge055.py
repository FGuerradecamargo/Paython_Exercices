list = [ ]
for p in range(1, 6):
    weight = float(input(f'Enter the {p} person weight: '))
    list.append(weight)

print(f'The bigger weight is: {max(list)} Kg\nThe smaller weight is: {min(list)}Kg')
