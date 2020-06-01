'''
Desafio para separar em lista a string: 012345678901234567890123456789012345678901234567890123456789
Utilizando list Comprehension
'''
string = '012345678901234567890123456789012345678901234567890123456789'
# for i in range(0, len(string), 10):
#     print(string[i:i+10] )
#     print(i)

n = 10
lista = [string[i:i+n] for i in range(0, len(string), n)]
print(lista)
retorno = '.'.join(lista)
print(retorno)
