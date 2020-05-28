'''
Formatando valore com modificadores
:s - Texto (string)
:d - Inteiros (int)
:f - Numero de ponto flutuante (float)
:.(numero)f - quantidade de casas decimais (float)
:(Caractere) (< ou > ou ^)(Quantidade)/TIPO - s,d ou f

> - Esquerda
< - Direita
^ - Centro
'''
# Formatando um numero
num = 43
print( f'{num:.2f}' )
print(f'{num:0>10.2f}') # coloca zeros a esquera e formata com 2 casas decimais
print()

nome = 'Dilson Mascarenhas'
print(f'{nome:-^50}')
print('{n:@>20}'.format(n=nome))

print()
print(nome.upper().center(50,'-'))