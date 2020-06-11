from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não esta ligado.'
            print(info)
            self.log_info(info)

        if self._conectado:
            error = f'{self._nome} JÁ ESTA CONECTADO.'
            print(error)
            self_error(error)
        info = f'{self._nome} ESTA CONECTADO.'
        print(info)
        self.log_info(info)

        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self_nome} não esta conectado.'
            print(error)
            log_error(error)

        info = f'{self_nome} FOI DESLIGADO COM SUCESSO.'
        print(info)
        log_info(info)

        self._conectado = False
