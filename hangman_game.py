import random

def jogar():
    abertura_jogo()
    palavra_secreta = cria_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas) #faz o layout da quantidade de letras
    loop_do_teste(palavra_secreta, letras_acertadas)

def abertura_jogo(): #printing the opening of the game
    print("*********************************")
    print("***Bem vindo no jogo de Forca!***")
    print("*********************************")

def cria_palavra_secreta(): #generates the random word using the words stored in the txt.
    with open("palavras.txt") as arquivo :
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra] #making the inicialization for the hangman game

def loop_do_teste(palavra_secreta, letras_acertadas):
    enforcou = False
    acertou = False
    erros = 0
    chute_repetido = [] #created this variable to store the guesses
    while (not enforcou and not acertou):
        chute = input("Qual letra ? \n").strip().upper() #getting the guess in a restrain format
        teste_chute(chute, chute_repetido) #checking the guess if it's possible
        chute_repetido.append(chute) #adding the guess for a list of tried guesses
        if (chute in palavra_secreta): #checking if the guess fits the word
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Você errou, agora são {} vidas!!!".format(7-erros))
            desenha_forca(erros)
        enforcou = erros == 7 #number of guesses
        acertou = "_" not in letras_acertadas #winning the game by not having _ inside of the list.
        print(letras_acertadas)
        print(chute_repetido)
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def imprime_mensagem_perdedor(palavra_secreta):  #the print for the loser
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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

def imprime_mensagem_vencedor(): #the print for the winner
    print("Parabéns, você ganhou!")
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

def desenha_forca(erros): #The print for the errors
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def teste_chute(chute, chute_repetido): #restrain the user to put any input that is not available
    while (len(chute) > 1): #restrain the number of characters
        print("Você pode colocar apenas 01 letra! Insira outra novamente : ")
        chute = input("Qual letra ? \n").strip().upper()
    while (chute in chute_repetido): #restrain any repeated input
        print("Você já colocou essa letra, insira outra novamente : ")
        chute = input("Qual letra ? \n").strip().upper()
    while (chute == ""): #restrain the the none input
        chute = input("Qual letra ? \n").strip().upper()
    return chute


if(__name__ == "__main__"):
    jogar()
