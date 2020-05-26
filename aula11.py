'''
analisando dados
isnumeric, isdigit, isdecimal = verifica se são numereos inteiros, retornando falspo para -1,3.22.
usando: try  e except
'''
n1 = input('Digite um numero: ')
n2 = input('Digite outro numero: ')

try:
    n1 = float(n1)
    n2 = float(n2)
    print( n1 + n2)
except:
    print('Error')
