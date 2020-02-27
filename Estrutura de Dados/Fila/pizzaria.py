from Fila.fila import Fila

class Pedido:

    def __init__(self, pizza):
        self.pizza = pizza

    def __repr__(self):
        return self.pizza

def main():

    pizzaria = Fila()

    pedido1 = Pedido("Muçarela")
    pedido2 = Pedido("Calabresa")
    pedido3 = Pedido("Marguerita")
    pedido4 = Pedido("Rúcula")

    pizzaria.entrar(pedido1)
    print("Recebendo pedido: {}".format(pedido1))

    pizzaria.entrar(pedido2)
    print("Recebendo pedido: {}".format(pedido2))

    pizzaria.entrar(pedido3)
    print("Recebendo pedido: {}".format(pedido3))


    pedido = pizzaria.sair()
    print("Fazendo a pizza de: {}".format(pedido))
    print("Está vazia? {}".format(pizzaria.vazia))

    pedido = pizzaria.sair()
    print("Fazendo a pizza de: {}".format(pedido))
    print("Está vazia? {}".format(pizzaria.vazia))

    pedido = pizzaria.sair()
    print("Fazendo a pizza de: {}".format(pedido))
    print("Está vazia? {}".format(pizzaria.vazia))

main()