def jogar_forca():

    print("*********************************")
    print("BEM VINDO AO JOGO DA FORCA!")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas =["_","_","_","_","_","_"]

    acertou = False
    enforcou = False


    # enquanto nao enforcou e nao acertou faça
    while(not enforcou and not acertou):

        chute = input("Qual letra...?")
        chute = chute.strip()# retira espacos em branco
        posicao = 0

        for letra in palavra_secreta:

            if (chute.upper()==letra.upper()):# coloca todas as letras em maiuscula
                letras_acertadas[posicao] = letra
                #print("Encontrei a letra {} na posição {}" .format(letra, index))
            posicao += 1

        print(letras_acertadas)
        letras_faltando = str(letras_acertadas.count("_"))
        print("Ainda faltam {} letras".format(letras_faltando))

    print("FIM DE JOGO")

if(__name__ == "__main__"):
    jogar_forca()






