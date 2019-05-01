import random
def jogar_forca():

    mensagem_abertura()# funcao da mensagem de boas vindas ao jogo
    palavra_secreta = carrega_palavra_secreta()# funcao do arquivo que contem a lista de palavras
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    acertou = False
    enforcou = False
    erros = 0

    # enquanto nao enforcou e nao acertou faça
    while(not enforcou and not acertou):
        chute = pede_chute() # chute do usuario
        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta) #chamada de funcao caso o chute esteja correto

        else:
            erros += 1
            print("Ops, vc errou!! Faltam {} tentativas." .format(6 - erros))

        if(erros == 6):
            break

        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

        letras_faltando = str(letras_acertadas.count("_"))
        print("Ainda faltam {} letras".format(letras_faltando))
    if(acertou):
        mensagem_vencedor()
    else:
        mensagem_perdedor()
    print("FIM DE JOGO")

""""------LISTA DE FUNCOES----"""

def mensagem_abertura():
    print("*********************************")
    print("BEM VINDO AO JOGO DA FORCA!")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("frutas.txt", 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):

    return ["_" for letra in palavra_secreta]# List comprehension dentro da lista

def pede_chute():
    chute: str = input("Qual a letra...?")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:

        if (chute.upper() == letra.upper()):  # coloca todas as letras em maiuscula
            letras_acertadas[posicao] = letra
            # print("Encontrei a letra {} na posição {}" .format(letra, index))
        posicao += 1

def mensagem_vencedor():
    print("VOCÊ GANHOU!!!")

def mensagem_perdedor():
    print("VOCÊ FOI ENFORCADO =(..")

if(__name__ == "__main__"):
    jogar_forca()








