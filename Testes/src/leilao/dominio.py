import sys
class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def propoe(self, lance: Lance):
        if lance.valor > self.maior_lance:
            self.maior_lance = lance.valor
        if lance.valor < self.menor_lance:
            self.menor_lance = lance.valor
        self.__lances.append(lance)

    @property
    def lances(self):
        return self.__lances[:]