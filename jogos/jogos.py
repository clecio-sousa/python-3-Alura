import adivinhacao
import forca

def escolhe_jogo():
    print("*********************************")
    print("ESCOLHA O SEU JOGO!")
    print("*********************************")

    print("(1)ADIVINHAÇÃO (2)FORCA")

    jogo = int(input("DIGITE A OPÇÃO ESCOLHIDA : "))

    if jogo == 1:

        print("JOGANDO ADIVINHAÇÃO")
        adivinhacao.jogar_adivinhacao()
    elif jogo == 2:
        print("JOGANDO FORCA")
        forca.jogar_forca()


if(__name__ == "__main__"):
    escolhe_jogo()()






