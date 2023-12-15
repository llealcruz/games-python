import adivinhacao
import forca


def escolher_jogo():
    print_msg_escolher_jogo()

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()


def print_msg_escolher_jogo():
    print("""
    +============================================================+
    | _____               _ _                                    |
    || ____|___  ___ ___ | | |__   __ _    ___    ___  ___ _   _ |
    ||  _| / __|/ __/ _ \| | '_ \ / _` |  / _ \  / __|/ _ \ | | ||
    || |___\__ \ (_| (_) | | | | | (_| | | (_) | \__ \  __/ |_| ||
    ||_____|___/\___\___/|_|_| |_|\__,_|  \___/  |___/\___|\__,_||
    |  (_) ___   __ _  ___ | |                                   |
    |  | |/ _ \ / _` |/ _ \| |                                   |
    |  | | (_) | (_| | (_) |_|                                   |
    | _/ |\___/ \__, |\___/(_)                                   |
    ||__/       |___/                                            |
    +============================================================+
    """)


if __name__ == "__main__":
    escolher_jogo()
