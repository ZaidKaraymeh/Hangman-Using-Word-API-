import utils.gameEngineFunctions as engine




def main():

    SIZE, word = engine.getWord()
    run = True
    tries = 5
    lettersGuessed = []

    print(f"The word has {SIZE} letters \nGood Luck!\n")

    while run:
        


        isGameEnded, message = engine.isGameEnded(lettersGuessed, word, tries)

        if isGameEnded:
            if not None:
                print(message)
                run = False
                break
            

        try:
            guess = input("Guess a letter: ")
            isFound, letters =   engine.isLetterFound(guess, word)
            if isFound:
                if not engine.isDuplicated(letters, lettersGuessed):

                    # map(lambda x: lettersGuessed.append(x), letters)
                    lettersGuessed += [x for x in letters]
                    print("\nletter", guess, "was found")
                else:
                    print("This letter is a duplicate")
            else:
                tries -= 1
                print(f"\nYou have {tries} tries left")

            print(engine.renderGuesses(lettersGuessed, word))
        except TypeError:
            run = False
        engine.renderMan(tries)
        



        
    print("Game has ended")


if __name__ == "__main__":
    main()

