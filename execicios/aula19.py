'''
Dicionário de perguntas e respostas
'''
print('-='*50)
cTitulo = ' Questionário de Avaliação '
print(f'{cTitulo:^100}')
print('-='*50)
print()
perguntas = {
        'pergunta 1' : {
            'pergunta': 'Quanto é 2 + 2 ?',
            'resposta': {'a': '1', 'b': '4','c':'5'},
            'certa'   : 'b',
        },
        'pergunta 2' : {
            'pergunta': 'Quanto é 2 * 3 ?',
            'resposta': {'a': '1', 'b': '4','c':'6'},
            'certa'   : 'c',
        },
}

resp_certas = 0

# laço do dicionario pergunta
for pk, pv in perguntas.items():
    print( f'{pk}: {pv["pergunta"]}')

    print('Resposta: ')
    for rk, rv in pv["resposta"].items():
        print(f'[{rk}]: {rv}')

    resp = input('Sua resposta: ')
    
    if resp == pv['certa']:
        print('Ehhh... Você ACERTOU !')
        resp_certas += 1
    else:
        print('Ahhh... você ERROU !')

    print()

print(f'Você acertou {resp_certas} resposta(s).')

qtd_perg = len(perguntas)
porc = resp_certas / qtd_perg * 100 
print(f'Sus porcentagem de acerto é de: {porc}%.')
