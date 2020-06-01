'''
Iniciar com letras, pode conter números, separar _, letras maíuscula
'''
nome = 'Dilson'
idade = 53
altura = 1.75
e_maior = idade > 18
peso = 80
imc = peso / (altura*altura)

print('Nome: ',nome)
print('Idade: ',idade)
print('Altura: ',altura)
print('Maior de Idade: ',e_maior)

print( nome, 'tem', idade, 'anos de idade e seu IMC é:', imc  )
print( f' {nome} tem {idade} anos de idade e seu IMC é: {imc:.2f}' )
print( ' {} tem {} anos de idade e seu IMC é: {:.2f}'.format( nome, idade, imc) )
print( ' {n} tem {i} anos de idade e seu IMC é: {im}'.format( n=nome, i=idade, im=imc) )
