'''
Faca um programa que peca ao usuario para digitar um numero inteiro, informe se este numero e par ou impar. Caso co usuário nao digire um numero inteiro, informe que não é um numero inteiro.

Faca um programa que pergunte a hora ao usuário e, baseando-se no horario descrito, exiba a sadação apropriada. Ex
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23

Faca um ´programa que peca o primeiro nome do usuario, se o nome tiver 4 letras ou menos, escreve "seu nome e curto"; se tiver entre 5 e 6 letras, escreva "Seu nome e normal"; maior que 6 escreva "Seu nome e grande".


# solução item 01
num = input('Digite um número: ')
try:
    num = int(num)
    if num % 2 == 0:
        print('Voce digitou um numero PAR')
    else:
        print('Voce digitou um numero IMPAR')
except:
    print('Você não digitou um numero inteiro.')

# Solução item 2
hora = input('Digite qual é a hora atual, usando entre 0 e 24: ')
try:
    if int(hora) <= 11:
        print('Bom dia!')
    elif int(hora) > 11 and int(hora) <= 17:
        print('Boa tarde!')
    else:
        print('Boa noite!')
except:
    print('Valor digitado INCORRETO !')
'''

# Solução item 3 
nome = input('Digite seu nome: ')
try:
    if len(nome) <= 3:
        print('Seu nome e curto.')
    elif len(nome) <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é grande!')
except expression as identifier:
    print('Error...')
