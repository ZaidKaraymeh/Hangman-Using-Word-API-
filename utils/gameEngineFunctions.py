import requests

def getWord():
    url = "https://random-words-api.vercel.app/word"

    response = requests.request("GET", url)

    word = response.json()[0].get("word")
    word = list(word)

    word = [x.lower() for x in word]

    for letter in word:
        if letter >= "a" and letter <= "z":
            None
        else:
            return getWord()



    return len(word), word

def isDuplicated(letters, lettersGuessed):
    
    for letter in lettersGuessed:
        for item in letters:
            if letter == item:
                return True
    
    return False

def isGameEnded(lettersGuessed, word, tries):
    if isCorrectAnswer(lettersGuessed, word):
        return True,"You won!"     
    
    
    if isTriesZero(tries):
        return True, "You Lost!"
    
    return False, None

def isCorrectAnswer(lettersGuessed, word):
    if len(lettersGuessed) == len(word):
        return True
    return False

def isTriesZero(tries):
    if tries == 0:
        return True
    return False

def isLetterFound(guess, word):
    letters = []
    
    for letter in word:
        if guess == letter:
            letters.append(letter)
    if len(letters) > 0:
        return True, letters
    return False, letters

def renderGuesses(guessedLetters, word):
    SIZE = len(word)
    guesses = ["_" for x in range(SIZE)]
    i = 0
    for item in word:
        for letter in guessedLetters:
            if letter == item:
                guesses[i] = letter
        i += 1 
    
    return guesses
        


def renderMan(tries):
    if tries == 5:
        print(" O")
        print("/|\\")
        print("/ \\")
    elif tries == 4:
        print(" O")
        print("/|")
        print("/ \\")
    elif tries == 3:
        print(" O")
        print(" |")
        print("/ \\")
    elif tries == 2:
        print(" O")
        print(" |")
        print("  \\")
    elif tries == 1:
        print(" O")
        print(" |")
        print("  ")
    elif tries == 0:
        print(" O")