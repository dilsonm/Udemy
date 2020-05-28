'''
Desafio:
    Suponha que temos um carinho com valior produtos e precos.
    Preciso que me retorne o total dos produtos que estão no carrinho.
'''
carrinho = []
carrinho.append(('Granpeador', 12))
carrinho.append(('Lapiseira', 8))
carrinho.append(('Caderno', 22))
carrinho.append(('Calculadora', 35))
carrinho.append(('Borracha', 3.18))
carrinho.append(('Caneta', 4.5))
carrinho.append(('Papel Sulfite', 28))

total = sum([ float(y) for x, y in carrinho ])
print(total)
# print( carrinho)
