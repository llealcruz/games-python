import random


def jogar():
    print_msg_boas_vindas()

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Parabéns, você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o número secreto")
            elif menor:
                print("Você errou! O seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("O número secreto era {}".format(numero_secreto))
    print("Fim do jogo!")


def print_msg_boas_vindas():
    print("""
     _____                                                             _____ 
    ( ___ )                                                           ( ___ )
     |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
     |   |      _                         _                            |   | 
     |   |     | | ___   __ _  ___     __| | ___                       |   | 
     |   |  _  | |/ _ \ / _` |/ _ \   / _` |/ _ \                      |   | 
     |   | | |_| | (_) | (_| | (_) | | (_| |  __/                      |   | 
     |   |  \___/ \___/ \__, |\___/   \__,_|\___|                      |   | 
     |   |            _ |___/   _       _                /\/|       _  |   | 
     |   |   __ _  __| (_)_   _(_)_ __ | |__   __ _  ___|/\/_  ___ | | |   | 
     |   |  / _` |/ _` | \ \ / / | '_ \| '_ \ / _` |/ __/ _` |/ _ \| | |   | 
     |   | | (_| | (_| | |\ V /| | | | | | | | (_| | (_| (_| | (_) |_| |   | 
     |   |  \__,_|\__,_|_| \_/ |_|_| |_|_| |_|\__,_|\___\__,_|\___/(_) |   | 
     |   |                                           )_)               |   | 
     |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
    (_____)                                                           (_____)
    """)


if __name__ == "__main__":
    jogar()
