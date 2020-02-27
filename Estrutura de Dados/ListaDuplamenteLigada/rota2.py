from ListaDuplamenteLigada.lista_duplamente_ligada import ListDuplamenteLigada, Celula

class Loja:

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return "* {} - {}".format(self.nome, self.endereco)

def situacao(lista):
    print("Quantidade: {}".format(lista.quantidade))
    lista.imprimir()

def main():

    loja1 = Loja("Mercadinho", "Rua das Laranjeiras, 12")
    loja2 = Loja("HortiFruti", "Rua do Pomar, 300")
    loja3 = Loja("Padaria", "Rua das Flores, 600")
    loja4 = Loja("Supermecado", "Alameda Santos, 400")
    loja5 = Loja("Mini Mercado", "Rua da Fazenda, 900")
    loja6 = Loja("Quitanda", "Avenida Rio Branco, 34")
    loja7 = Loja("Minimercado das Frutas", "Avenida do Bosque, 66")
    loja8 = Loja("SF", "Avenida Rio Branco, 600")
    loja9 = Loja("Supermercado das Frutas", "Rua do Pomar, 800")
    loja10 = Loja("Hortifruti da Terra", "Rua das Laranjeira, 800")

    lista = ListDuplamenteLigada()

    lista.inserir_no_inicio(loja1)
    lista.inserir_no_inicio(loja2)
    lista.inserir_no_inicio(loja3)
    lista.inserir_no_fim(loja4)
    lista.inserir_no_fim(loja5)
    lista.inserir_no_fim(loja6)
    lista.inserir_em_qualquer_posicao(2, loja7)
    lista.inserir_em_qualquer_posicao(7, loja8)
    lista.inserir_em_qualquer_posicao(0, loja9)
    lista.inserir_em_qualquer_posicao(6, loja10)

    situacao(lista)

    removido = lista.remover_do_inicio()
    print("Removido do inicio: {}".format(removido))

    situacao(lista)

    removido = lista.remover_do_fim()
    print("Removido do fim: {}".format(removido))

    situacao(lista)

    removido = lista.remover_em_qualquer_posicao(1)
    print("Removido da posição 1: {}".format(removido))

    situacao(lista)

    removido = lista.remover_em_qualquer_posicao(5)
    print("Removido da posição 5: {}".format(removido))

    situacao(lista)

    removido = lista.remover_em_qualquer_posicao(0)
    print("Removido da posição 0: {}".format(removido))

    situacao(lista)


main()