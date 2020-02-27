class Celula:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None
        self.anterior = None

class ListDuplamenteLigada:

    def __init__(self):
        self._inicio = None
        self._fim = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio
    @property
    def fim(self):
        return self._fim
    @property
    def quantidade(self):
        return self._quantidade

    def _inserir_em_lista_vazia(self, conteudo):
        celula = Celula(conteudo)
        self._inicio = celula
        self._fim = celula
        self._quantidade += 1

    def inserir_no_inicio(self, conteudo):
        if self._quantidade == 0:
            return self._inserir_em_lista_vazia(conteudo)
        else:
            celula = Celula(conteudo)
            celula.proximo = self._inicio
            self._inicio.anterior = celula
            self._inicio = celula
            self._quantidade += 1

    def inserir_no_fim(self, conteudo):
        if self._quantidade == 0:
            return self._inserir_em_lista_vazia(conteudo)
        else:
            celula = Celula(conteudo)
            celula.anterior = self._fim
            self._fim.proximo = celula
            self._fim = celula
            self._quantidade += 1

    def inserir_em_qualquer_posicao(self, posicao, conteudo):
        if posicao == 0:
            return self.inserir_no_inicio(conteudo)
        if posicao == self._quantidade:
            return self.inserir_no_fim(conteudo)
        esquerda = self._celula(posicao - 1)
        direita = esquerda.proximo
        celula = Celula(conteudo)
        celula.proximo = direita
        celula.anterior = esquerda
        esquerda.proximo = celula
        direita.anterior = celula
        self._quantidade += 1

    def _remover_ultimo(self):
        if self._quantidade ==  1:
            removido = self._inicio
            self._inicio = None
            self._fim = None
            self._quantidade -= 1
            return removido.conteudo

    def remover_do_inicio(self):
        if self._quantidade == 1:
            return self._remover_ultimo()
        else:
            removido = self._inicio
            self._inicio = removido.proximo
            self._inicio.anterior = None
            removido.proximo = None
            self._quantidade -= 1
            return removido.conteudo

    def remover_do_fim(self):
        if self._quantidade == 1:
            return self._remover_ultimo()
        else:
            removido = self._fim
            self._fim = removido.anterior
            self._fim.proximo = None
            removido.anterior = None
            self._quantidade -= 1
            return removido.conteudo

    def remover_em_qualquer_posicao(self, posicao):
        if posicao == 0:
            return self.remover_do_inicio()
        if posicao == self.quantidade - 1:
            return self.remover_do_fim()
        removido = self._celula(posicao)
        esquerda = removido.anterior
        direita = removido.proximo
        removido.proximo = None
        removido.anterior = None
        esquerda.proximo = direita
        direita.anterior = esquerda
        self._quantidade -= 1
        return removido.conteudo

    def item(self, posicao):
        celula = self._celula(posicao)
        return celula.conteudo

    def _validar_posicao(self, posicao):
        if 0<= posicao < self._quantidade:
            return True
        raise IndexError("Posição inválida: {}".format(posicao))

    def _celula(self, posicao):
        self._validar_posicao(posicao)
        metade = self._quantidade // 2
        if posicao < metade:
            atual = self._inicio
            for i in range(0, posicao):
                atual = atual.proximo
            return atual
        else:
            atual = self._fim
            for i in range(posicao + 1, self._quantidade)[::-1]:
                atual = atual.anterior
            return atual


    def imprimir(self):
        atual = self._inicio
        for i in range(0, self._quantidade):
            print(atual.conteudo)
            atual = atual.proximo

