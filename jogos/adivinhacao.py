import random
def jogar_adivinhacao():

    print("*********************************")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO!")
    print("*********************************")



    numero_secreto = random.randrange(100) # FUNCAO RANDOM QUE GERA NUMEROS ALEATORIOS DE 0 A 99
    #print(numero_secreto)
    tentativas = 0

# O JOGADOR ESCOLHE SEU NIVEL DE DIFICULDADE
    print("QUAL O NÍVEL DE DIFICULDADE:")
    print("(1) FÁCIL")
    print("(2) MÉDIO")
    print("(3) DIFÍCIL")

    pontos = 1000 # ELE COMEÇA INICIALMENTE COM 1000 PTS
    nivel = int(input("DIGITE O NÍVEL DESEJADO:"))

    if (nivel==1):
        tentativas = 20 # NRO DE TENTATIVAS
    elif (nivel == 2):
        tentativas = 10 #NRO DE TENTATIVAS

    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("tentativa {} de {}".format(rodada, tentativas))# INTERPOLACAO DE STRINGS INDICANDO O NRO DA RODADA E DE TENTATIVAS
        chute_str = input("Digite um numero:")
        print("Você digitou:", chute_str)
        chute = int(chute_str)#CONVERTE STRING PARA INT

        if (chute < 1 or chute > 100):
            print("Vc deve digitar um numero entre 0 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Vc acertou e fez {} pontos".format(pontos))
            break

        else:
            if(menor):
                print("o numero eh maior")

            elif(maior):
                print("O numero eh menor")
            pontos_perdidos = abs(numero_secreto - chute)#INCLUSAO DA FUNCAO ABS PRA EVITAR QUE HAJANRO NEGATIVO
            pontos = pontos - pontos_perdidos #TOTAL DE PONTOS


    print("O numero era ", numero_secreto)
    print("FIM DE JOGO")

if(__name__=="__main__"):
    jogar_adivinhacao()






