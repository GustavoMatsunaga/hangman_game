import random

def play_hangman ():
    welcome_layout()
    random_word = making_random_word()
    guess_random_word = layout_guess_word(random_word)
    tried_words = []
    life = 8
    discovered_word = False
    dead = False
    while (not discovered_word and not dead): #looping for the game
        guess = making_right_guess(tried_words)
        tried_words.append(guess)
        if (guess in random_word):          #first check if it's in the random word
            index = 0
            for letter in random_word:      #finding where to put the words
                if (guess == letter):
                    guess_random_word[index] = letter
                index += 1
            print(guess_random_word)
        else:
            life -= 1
            layout_hangman(life)
        if("_" not in guess_random_word):    #if no more blank spaces the word has been discovered
            discovered_word = True
            winner_trophy()
        elif(life == 0):                    #no mores lifes = DEAD!
            dead = True
            death_message(random_word)

def welcome_layout():                       #layout for the begining of the game
    print("**************************************")
    print("****WELCOME TO THE HANGMAN GAME!!!****")
    print("**************************************")
    print("IT'S A FRUIT!!!")


def making_random_word():                   #chooses a word from the words.txt
    with open("words.txt") as file:
        words = []
        for line in file:
            line = line.strip().upper()
            words.append(line)
        random_number = random.randint(0, len(words))
    return words[random_number]

def layout_guess_word(random_word):         #make the layout (spaces) for the guessing game
    layout_random_word = []
    for letter in random_word:
        if(letter == " "):
            layout_random_word.append(" ")
        else:
            layout_random_word.append("_")
    print(layout_random_word)
    return layout_random_word

def making_right_guess (tried_words):       #restrain the user to put the right inputs
    check_guess = input("Please, enter your letter : ").strip().upper()
    while(True):
        if (not check_guess.isalpha() or (len(check_guess) > 1)):   #checking if it's a letter
                print("Wrong input!!")
                check_guess = input("Please, enter your letter : ").strip().upper()
        elif(check_guess in tried_words):                   #checking if the letter has already been used
                print("You have already entered this!! ")
                check_guess = input("Please, enter your letter : ").strip().upper()
        elif (len(check_guess) > 0):
            return check_guess

def death_message(random_word):  #the print for the loser
    print("Sorry, you have been hanged!")
    print("The word was {}".format(random_word))
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

def winner_trophy(): #the print for the winner
    print("CONGRATULATIONS, YOU HAVE WON!")
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

def layout_hangman(life): #The print for the mistakes
    print("  _______     ")
    print(" |/      |    ")

    if(life == 7):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(life == 6):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(life == 5):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(life == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(life == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(life == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (life == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == '__main__':
    play_hangman()
