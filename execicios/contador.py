from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'José', 'nota': 'B'},
]
ordena = lambda item: item['nota']  
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos,ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'Agrupoamento: {agrupamento}')

    for alunos in va1:
        print(f'\t{alunos}')

    quantidade = len(list(va2))
    print(f'{quantidade} alunos tiraram nota {agrupamento}')
    
    print()
