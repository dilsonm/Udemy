'''
Utilizando ZIP e ZIP_LONGEST
ZIP - Padrão Paython
ZIP_LONGEST - pertence a biclioteca 
'''
from itertools import zip_longest, count

indice = count()

cidades = ['São Paulo','Belo Horizonte','Salvador','Monte Belo','Outra' ]
estados = ['SP','MG','BA']

cidade_estado = zip(
    indice,
    estados,
    cidades,
)

for indice, estado, cidade in cidade_estado:
    print(indice, estado, cidade)

