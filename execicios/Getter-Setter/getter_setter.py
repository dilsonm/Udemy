class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # Getter

    @property
    def preco(self):
        return self._preco

    # Setter

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('RS', ''))
        self._preco = valor


p1 = produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = produto('CANECA', 'RS15')
p2.desconto(10)
print(p1.nome, p2.preco)

p3 = produto('Calça', 150)
p3.desconto(15)
print(p3.nome, p3.preco)

