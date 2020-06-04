'''
Ler / Escrever arquivos
https://https://docs.python.org/3/library/functions.html#open
Parametros de OPEN:
w+  -   leitura e escrita
r   -   leitura
a+  -   append (adiciona mais coisas ao arquivo)

'''
import os
import json

d1 = {
    'Pessoa1' : {
        'nome': 'Dilson',
        'idade': 53,
    },
    'Pessoa2' : {
        'nome': 'Rosana',
        'idade': 53,
    },
}
print(d1)
d1_json = json.dumps(d1, indent=True)
print(d1_json)

with open('abc.json','w+') as file:
    file.write(d1_json)


'''
with open('exemplo.txt','w+') as file:
    file.write('Linha 1\n') 
    file.write('Linha 2\n') 
    file.write('Linha 3\n') 

    file.seek(0)
    print(file.read())

# apagando o arquivo
# os.remove('exemplo.txt')

file = open('exemplo.txt','w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('Lendo arquivo...')
print(file.read())
print('###################')
file.seek(0, 0)
print(file.readline(),end='')
print(file.readline(),end='')
print(file.readline(),end='')

print('-----------------')
file.seek(0, 0)
for linha in file:
    print(linha,end='')
file.close()
'''
