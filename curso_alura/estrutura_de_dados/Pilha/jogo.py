from Pilha.pilha import Pilha

class Fase:

    def __init__(self, cenario, pontuacao, punicao):
        self.cenario = cenario
        self.pontuacao = pontuacao
        self.punicao = punicao

    def __repr__(self):
        return self.cenario

def main():
    fases = Pilha()
    fase1 = Fase("Floresta", 300, -100)
    fase2 = Fase("Castelo", 300, -4)
    fase3 = Fase("Caverna", 400, -50)
    fase4 = Fase("Guerra", 3000, -400)

    fases.empilha(fase1)
    fases.empilha(fase2)
    fases.empilha(fase3)
    fases.empilha(fase4)

    falhou = fases.desempilha()
    print("Falhou na fase: ")
    print(falhou)
    print("Voltou para a fase:")
    print(fases.ver_topo)

    falhou = fases.desempilha()
    print("Falhou na fase: ")
    print(falhou)
    print("Voltou para a fase:")
    print(fases.ver_topo)


main()