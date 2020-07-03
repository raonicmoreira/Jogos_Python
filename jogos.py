import adivinhacao
import forca

def escolha_jogo():
    print("*********************************")
    print("        Escolha o seu jogo       ")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo?"))

    if jogo == 1:
        print("Jogo da forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogo de adivinhação")
        adivinhacao.jogar()
if(__name__ == "__main__"):
    escolha_jogo()