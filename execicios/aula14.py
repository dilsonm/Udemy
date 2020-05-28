'''
Jogo palavra secreta
'''
palavra = 'brasileiro'
pcerta = ''
contador = 0

while True:
    letra = input('Digite uma letra: ')
    if len(letra) != 1:
        print('Não vale, voce digitou mais que um caracater')

    secreto = ''
    for c in palavra:
        if letra in c:
            secreto += c
        else:
            ...
            secreto += '*'

    print(secreto)

    # if letra in palavra:
    #      print('Você acertou !!!')
    # else:
    #     print('Voce ERROUUUU...')

    if contador >= 10:
        print('Voce PERDEU... HAHAHAHA.')
        break
    else:
        contador += 1
