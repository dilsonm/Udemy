'''
* Criar variaveis para nome(str), idade(int),
* altura (float), e peso (float) de uma pessoa
* Criar variavel como o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e ano atual da pessoa)
* Exibir um texto com todos os valores na tela usando f-string (com as chaves).
'''
nome = 'Dilson'
idade = 53
altura = 1.75
peso = 80.5
ano = 2020
imc = peso / (altura * altura)
nasc = ano - idade
print(f'{nome} tem {idade} anos de idade, sua altura é de {altura}, seu peso {peso} e seu IMC é: {imc:.2f}')
print(f'O ano de nascimento da pessoa é: {nasc}')
