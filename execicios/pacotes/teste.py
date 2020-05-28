# 1) import vendas.calc_preco
# 2) from vendas import calc_preco
from vendas.calc_preco import aumento, reducao

preco = 49.90
# 1) print(vendas.calc_preco.aumento(preco,15))
# 2) print( calc_preco.aumento(preco,15))
print( aumento(preco,15,formata=True))
print( reducao(preco,25,formata=True))
