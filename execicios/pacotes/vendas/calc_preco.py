# from formata.preco import real
from vendas.formata import preco

def aumento(valor, porcentagem, formata=False):
    r = valor + (valor * porcentagem /100)
    return preco.real(r) if formata else r

def reducao(valor, porcentagem, formata=False):
    r = valor - (valor * porcentagem /100)
    return preco.real(r) if formata else r

if __name__ == '__main__':
    print(aumento(100,10,formata=True))
    print(reducao(100,10))
