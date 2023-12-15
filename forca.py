import random


def jogar():
    print_msg_boas_vindas()

    palavra_secreta = gerar_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    total_tentativas = 7

    print("Palavra com {} letras".format(len(palavra_secreta)))

    while not enforcou and not acertou:
        print("Você quer chutar uma letra ou a palavra?")
        print("(1) Letra (2) Palavra")
        codigo_chute = obter_codigo_chute()

        if codigo_chute == 1:
            letra_chute = input("Digite uma LETRA: ").strip().upper()
            if letra_chute in palavra_secreta:
                marcar_chute_correto(letra_chute, letras_acertadas, palavra_secreta, erros)
            else:
                erros = marcar_chute_errado(erros, letras_acertadas, total_tentativas)
        else:
            palavra_chute = input("Digite uma PALAVRA: ").strip().upper()
            if palavra_chute == palavra_secreta:
                letras_acertadas = palavra_chute
            else:
                erros = marcar_chute_errado(erros, letras_acertadas, total_tentativas)

        enforcou = total_tentativas - erros <= 0
        acertou = "_" not in letras_acertadas

    if acertou:
        print_msg_vencedor()
    else:
        print_msg_perdedor(palavra_secreta)


def marcar_chute_errado(erros, letras_acertadas, total_tentativas):
    erros += 1
    desenha_forca(erros)
    print("Você errou!")
    print_msg_acerte(letras_acertadas)
    return erros


def marcar_chute_correto(letra_chute, letras_acertadas, palavra_secreta, erros):
    index = 0
    for letra in palavra_secreta:
        if letra == letra_chute:
            letras_acertadas[index] = letra_chute
        index += 1
    desenha_forca(erros)
    print("Você acertou a letra!")
    print_msg_acerte(letras_acertadas)


def gerar_palavra_secreta():
    arquivo = open("palavras.txt", encoding="UTF-8")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()
    random_index = random.randrange(0, len(palavras))
    palavra_secreta = palavras[random_index].upper()
    return palavra_secreta


def obter_codigo_chute():
    codigo_correto = False
    codigo_chute = ""
    while not codigo_correto:
        entrada_usuario = input("Digite o código: ").strip()
        msg_cod_incorreto = "Opção inválida. Escolha 1 para letra ou 2 para palavra."
        if entrada_usuario.isdigit():
            codigo_chute = int(entrada_usuario)
            if codigo_chute not in [1, 2]:
                print(msg_cod_incorreto)
                continue
            codigo_correto = True
        else:
            print(msg_cod_incorreto)
            codigo_correto = False
    return codigo_chute


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def print_msg_acerte(letras_acertadas):
    print("Acerte a palavra: {}".format(letras_acertadas))


def print_msg_boas_vindas():
    print("""
     _____                                                                    _____ 
    ( ___ )                                                                  ( ___ )
     |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
     |   |      _                         _         __                     _  |   | 
     |   |     | | ___   __ _  ___     __| | ___   / _| ___  _ __ ___ __ _| | |   | 
     |   |  _  | |/ _ \ / _` |/ _ \   / _` |/ _ \ | |_ / _ \| '__/ __/ _` | | |   | 
     |   | | |_| | (_) | (_| | (_) | | (_| |  __/ |  _| (_) | | | (_| (_| |_| |   | 
     |   |  \___/ \___/ \__, |\___/   \__,_|\___| |_|  \___/|_|  \___\__,_(_) |   | 
     |   |              |___/                                                 |   | 
     |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
    (_____)                                                                  (_____)
    """)


def print_msg_perdedor(palavra_secreta):
    print("Tentativas esgotadas, você PERDEU.")
    print("A palavra era: {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def print_msg_vencedor():
    print("Parabéns, você VENCEU o jogo!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
