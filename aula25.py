'''
count - itertools
'''
from itertools import count

contador = count()
# contador = count( start=0 step=2 )  # cudado para não deixar em loop infinito
lista = ['Luiz','João', 'Maria', 'José', 'Silva', 'Edurado']

lista = zip(contador, lista)
print(list(lista))
