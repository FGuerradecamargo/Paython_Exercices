weights = []

for p in range(1, 6):
    weight = float(input(f'Enter the {p} person weight: '))
    weights.append(weight)

print(f'The bigger weight is: {max(weights)} Kg\nThe smaller weight is: {min(weights)}Kg')
