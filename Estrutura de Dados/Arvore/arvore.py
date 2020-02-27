from ListaDuplamenteLigada.lista_duplamente_ligada import ListDuplamenteLigada

class ListaDeNodos(ListDuplamenteLigada):

    def __init__(self):
        super().__init__()

    def imprimir(self, nivel):
        atual = self._inicio
        for i in range(0, self._quantidade):
            atual.conteudo.imprimir(nivel)
            atual = atual.proximo

    def localizar_nodo(self, conteudo):
        atual = self._inicio
        for i in range(0, self._quantidade):
            encontrado = atual.conteudo.localizar_nodo(conteudo)
            if encontrado:
                return encontrado
            atual = atual.proximo

    def posicao(self, conteudo):
        atual = self._inicio
        for i in range(0, self._quantidade):
            if atual.conteudo.conteudo == conteudo:
                return i
            atual = atual.proximo


class Nodo:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.pai = None
        self.filhos = None

    def __repr__(self):
        return self.conteudo

    def imprimir(self, nivel=0):
        print("{} - {}".format(" "*nivel,self.conteudo))
        if self.filhos:
            self.filhos.imprimir(nivel + 1)

    def inserir_filho(self, filho):
        if self.filhos is None:
            self.filhos = ListaDeNodos()
        nodo = Nodo(filho)
        nodo.pai = self
        self.filhos.inserir_no_fim(nodo)

    def localizar_nodo(self, conteudo):
        if conteudo == self.conteudo:
            return self
        if self.filhos:
            return self.filhos.localizar_nodo(conteudo)

    def remover(self):
        if self.pai:
            posicao = self.pai.filhos.posicao(self.conteudo)
            return self.pai.filhos.remover_em_qualquer_posicao(posicao)
        return self

class Arvore:

    def __init__(self, conteudo):
        self.raiz = Nodo(conteudo)

    def imprimir(self):
        self.raiz.imprimir()

    def localizar_nodo(self, conteudo):
        return self.raiz.localizar_nodo(conteudo)

    def inserir_nodo(self, pai, filho):
        nodo_pai = self.localizar_nodo(pai)
        if nodo_pai:
            nodo_pai.inserir_filho(filho)

    def remover_nodo(self, conteudo):
        encontrado = self.raiz.localizar_nodo(conteudo)
        if encontrado:
            if encontrado is self.raiz:
                self.raiz = None
            else:
                encontrado.remover()
        return encontrado
