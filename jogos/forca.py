import random
def jogar_forca():

    print("*********************************")
    print("BEM VINDO AO JOGO DA FORCA!")
    print("*********************************")

    arquivo = open("frutas.txt", 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0,len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas =["_" for letra in palavra_secreta]# List comprehension dentro da lista

    acertou = False
    enforcou = False
    erros = 0


    # enquanto nao enforcou e nao acertou faça
    while(not enforcou and not acertou):

        chute = input("Qual letra...?")
        chute = chute.strip().upper()# retira espacos em branco

        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:

                if (chute.upper()==letra.upper()):# coloca todas as letras em maiuscula
                    letras_acertadas[posicao] = letra
                    #print("Encontrei a letra {} na posição {}" .format(letra, index))
                posicao += 1
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
        print("VOCE GANHOU!!")
    else:
        print("VC PERDEU!!!")
    print("FIM DE JOGO")

if(__name__ == "__main__"):
    jogar_forca()








