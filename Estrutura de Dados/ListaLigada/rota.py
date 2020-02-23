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

    print("======== Inserções ========\n")
    lista.imprimir()
    print("\nQuantidade de itens: ", end="")
    print(lista.quantidade)

    print("\n\n======== Remoções no início ========\n")
    removido = lista.remover_inicio()
    print("Removido: {}".format(removido))
    removido = lista.remover_inicio()
    print("Removido: {}".format(removido))
    print("\nQuantidade de itens: ", end="")
    print(lista.quantidade)

    print("\n\n======== Remoções em qualquer posição ========\n")

    removido = lista.remover_em_qualquer_posicao(2)
    print("Removido da posicao 2: {}".format(removido))
    removido = lista.remover_em_qualquer_posicao(0)
    print("Removido da posicao 0: {}".format(removido))

    print("\n\n======== Lista Resultante ========\n")
    lista.imprimir()
    print("\nQuantidade de itens: ", end="")
    print(lista.quantidade)

    print("\n\n========Printando na posição específica ========\n")
    print(lista.item(0))

main()
