class Orcamento(object):
    def __init__(self, valor) -> None:
        self.__valor = valor
    
    @property
    def valor(self):
        return self.__valor

orcamento = Orcamento(500)
orcamento.valor