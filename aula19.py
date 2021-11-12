pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f"o {pessoas['nome']} tem {pessoas['idade']} anos")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['peso'] = 98.5
print('=' * 65)
for k,v in pessoas.items():
    print(f'{k} = {v}')
print('=' * 65)
estado = {}
brasil = []
for c in range(0,2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')