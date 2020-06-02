"""
Public, Protected, Private
_ Privado / protected (public _)
__ privado (_NOMEDACLASSE__nomeatributo)
"""


class basededados:
    def __init__(self):
        self.__dados = {}

    def inserirCliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id, nome}
        else:
            self.__dados['clientes'].update({id, nome})

    def listaClientes(self):
        for id, nome in self.__dados.items():
            print(id, nome)

    def apagaCliente(self, id):
        del self.__dados['clientes'][id]


bd = basededados()
bd.inserirCliente(1, 'Otávio')
bd.inserirCliente(2, 'Miranda')
bd.inserirCliente(3, 'Dlson')
bd.listaClientes()
print(bd._basededados__dados)
