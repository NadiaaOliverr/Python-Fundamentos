import random


def jogar():
    print("********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000
    rodada = 0

    print("Qual o nível de dificuldade?")
    print("(1) Fácil\n(2) Médio\n(3) Difícil")

    nivel = int(input("Defina o nível: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    while (rodada < total_de_tentativas):
        rodada += 1
        print("Tentativa {0} de {1}".format(rodada, total_de_tentativas))
        chute = input("Digite o seu número: ")
        chute = int(chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {}".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()
