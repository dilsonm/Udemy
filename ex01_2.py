'''
Operadores lógico
AND
OR 
NOT
IN
NOT IN
'''
nome = input('Qual o seu nome: ')
idade = input('Qual a sua idade: ')
variavel = 'son'
i = int(idade)
print('-='*50)
# if i > 18 and i < 20:
#     print('Seja em vindo jovem.')
# else:
#     print('Seja bem vindo senhor.')

if variavel in nome:
    print(f'em seu nome: {nome} temos a expresão "son')
else:
    print(f'em seu nome: {nome} NÃO temos a expresão "son')


print('-='*50)

