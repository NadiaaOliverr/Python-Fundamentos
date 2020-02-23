from lista_ligada import ListaLigada, Celula

class Loja:

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return "{}\n {}".format(self.nome, self.endereco)

def main():

    loja1 = Loja("Mercadinho", "Rua das Laranjeiras, 12")
    loja2 = Loja("HortiFruti", "Rua do Pomar, 300")
    loja3 = Loja("Padaria", "Rua das Floes, 600")
    loja4 = Loja("Supermecado", "Alameda Santos, 400")
    loja5 = Loja("Mini Mercado", "Rua da Fazenda, 900")
    loja6 = Loja("Quitanda", "Avenida Rio Branco, 34")

    lista = ListaLigada()

    lista.inserir_no_inicio(loja1)
    lista.inserir_no_inicio(loja2)
    lista.inserir_no_inicio(loja3)
    lista.inserir_no_inicio(loja4)

    lista.inserir_em_qualquer_posicao(1,loja2)
    lista.imprimir()

    removido = lista.remover_inicio()
    print("Removido: {}".format(removido))
    removido = lista.remover_inicio()
    print("Removido: {}".format(removido))
    print(lista.quantidade)

    lista.imprimir()


main()
