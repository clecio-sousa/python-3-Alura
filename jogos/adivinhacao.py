import random

print("*********************************")
print("BEM VINDO AO JOGO DE ADIVINHAÇÃO!")
print("*********************************")

numero_secreto = random.randrange(100) # FUNCAO RANDOM QUE GERA NUMEROS ALEATORIOS DE 0 A 99
print(numero_secreto)
tentativas = 3

for rodada in range(1, tentativas + 1):
    print("tentativa {} de {}".format(rodada, tentativas))
    chute_str = input("Digite um numero:")
    print("Você digitou:", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Vc deve digitar um numero entre 0 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Vc acertou")
        break

    elif (menor):
        print("o numero eh maior")

    elif (maior):
        print("O numero eh menor")


random.random()
print("FIM DE JOGO")






