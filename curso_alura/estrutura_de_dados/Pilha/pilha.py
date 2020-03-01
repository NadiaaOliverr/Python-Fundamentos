from ListaLigada.lista_ligada import ListaLigada

class Pilha:

    def __init__(self):
        self.pilha = ListaLigada()

    def empilha(self, conteudo):
        self.pilha.inserir_no_inicio(conteudo)

    def desempilha(self):
        return self.pilha.remover_inicio()

    @property
    def ver_topo(self):
        return self.pilha.item(0)

    @property
    def pilha_vazia(self):
        return self.pilha.quantidade == 0