from datetime import date
dic = {}
dic['name'] = str(input('Name: ')).strip()
birth = int(input('Year of birth: '))
dic['age'] = date.today().year - birth
dic['ctps'] = int(input('Worker inscription (enter 0 if you so not have one: '))
if dic['ctps'] != 0:
    dic['year of hiring'] = int(input('Year of hiring: '))
    dic['salary'] = float(input('Salary: € '))
    dic['retirement'] = (dic['year of hiring'] + 35) - birth
print('-=' * 35)
for k, v in dic.items():
    print(f'  - {k} has the value {v}')
