'''
-> É uma lista de numeros inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas tem os numeros entre 1 - 10 e eles podem ser diplicados

-> crie uma função que encontre o numero duplicado considerando o segundo número com a duplicação. retorne a duplicação considerada.

---- Requisitos ----
A ordem do número duplicado e considerada a partir do segundo
Ocorrencia do numero, ou seja, o numero duplicado em si
Exemplo: 
    [1, 2, 3, 3, 2, 1] os numeros: 1, 2 e 3 são duplicados, retorne = 3
    [1, 2, 3, 4, 5, 6] retorno -1, nao tem numeros duplicados.
'''
lista_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,6,8,],
    [1,3,2,2,8,6,5,9,6,7],
    [3,8,2,8,6,7,7,3,1,9],
    [4,8,8,8,5,1,10,3,1,7],
    [1,3,7,2,2,1,5,1,9,9],
    [10,2,2,1,3,5,10,5,10,1],
    [1,6,1,5,1,1,1,4,7,3],
    [1,3,7,1,10,5,9,2,5,7],
    [4,7,6,5,2,9,2,1,2,1],
    [5,3,1,8,5,7,1,8,8,7],
    [10,9,8,7,6,5,4,3,2,1],
]

for c, v in enumerate(lista_inteiros):

    dup = -1
    lista_nova = []
    for x, v in enumerate(v):

        if v in lista_nova:
            dup = v
            print(f'Valor duplicado na lista {lista_inteiros[c]} foi o {dup}')
            break
        else:
            lista_nova.append(v)

    if dup == -1:
        print(f'Valor duplicado na lista {lista_inteiros[c]} foi o {dup}')


"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
"""

