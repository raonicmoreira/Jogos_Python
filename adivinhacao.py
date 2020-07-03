import random

def jogar():
    print("*********************************")
    print("bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    rodada = 1
    pontuacao = 1000

    print("Escolha o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Informe o nível que deseja jogar :"))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    while rodada <= total_de_tentativas:
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite um numero entre 1 e 100")
        print("Você digitou: ", chute)
        chute_convertido = int(chute)

        if chute_convertido < 1 or chute_convertido > 100:
            print("Você deve digitar um valor entre 1 e 100")
            continue

        acertou = numero_secreto == chute_convertido
        maior   = numero_secreto < chute_convertido

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontuacao))
            break
        elif maior:
            print("Você errou, seu chute foi maior que o valor secreto!")
        else:
            print("Você errou, seu chute foi menor que o valor secreto!")
        pontos_perdidos = abs(numero_secreto - chute_convertido)
        rodada = rodada +1
        pontuacao = pontuacao - pontos_perdidos

    print("*********************************")
    print("           FIM DO JOGO!          ")
    print("*********************************")
if(__name__ == "__main__"):
    jogar()