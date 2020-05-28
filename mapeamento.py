from dados import produtos, pessoas, lista

def aumento_preco(p):
    p['preco'] = round( p['preco'] * 1.05,2)
    return p

# precos = map(lambda p: p['preco'], produtos)
# precos = map(aumento_preco, produtos)
nomes = map(lambda p: p['nome'], pessoas)
for preco in nomes:
    print(preco)


# for produto in produtos:
#     print(produto)
