from ListaDuplamenteLigada.lista_duplamente_ligada import ListDuplamenteLigada

class Fila:

    def __init__(self):
        self.fila = ListDuplamenteLigada()

    def entrar(self, conteudo):
        self.fila.inserir_no_fim(conteudo)

    def sair(self):
        return self.fila.remover_do_inicio()

    @property
    def vazia(self):
        return  self.fila.quantidade == 0