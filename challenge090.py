dic = {}

dic['name'] = str(input('Name: ')).strip()
dic['average'] = float(input(f"{dic['name']}'s average: "))
if dic['average'] >= 7:
    dic['situation'] = 'Approved'
elif 5 <= dic['average'] < 7:
    dic['situation'] = 'Under recovery'
else:
    dic['situation'] = 'Reproved'
print('=' * 30)
for k, v in dic.items():
    print(f'{k} is igual {v}')
