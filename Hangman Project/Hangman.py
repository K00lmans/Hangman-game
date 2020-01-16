import random


def word_loader():
    """Loads a random word from the word list."""
    # Opens the word list document and puts into a list format
    with open("words.txt") as file:
        lines = file.readlines()
    randNum = random.randint(1, len(lines) - 1) # Selects a random number from 1 to the number of words
    return lines[randNum][:-1] # Removes the trailing new line


def word_updater(guessedLetters, word):
    """Takes an input and makes sure its clean."""
    global guessCount
    while True:
        userData = input("What letter would you like to guess? ")
        userData.lower() # Makes all letters in the input lower case
        # Checks if a letter has been guessed before
        if userData in guessedLetters:
            print("You have guessed that letter before, please use another letter.")
        # Checks if there is more than one letter
        elif len(userData) != 1:
            print("Please enter only one letter.")
        # Check if it contains only letters
        elif not userData.isalpha():
            print("Please only enter letters.")
        else:
            guessedLetters.append(userData)
            if userData not in word:
                guessCount = guessCount - 1
            return guessedLetters


def info_adder(wordData, guessedLetters):
    """Fills wordData with the revealed letters."""
    for letter in enumerate(word):
        # If the letter in the word is in guessedLetters, set that locatin in wordData with that letter
        if letter[1] in guessedLetters:
            wordData[letter[0]] = letter[1]
    return wordData


def word_printer(word, guessCount, guessedLetters):
    """Prints out unerscores for unguessed letters and the letter for correctly guessed letters."""
    wordData = [] # An empty list to store what letters have been guessed
    # Fills the empty list with underscores
    for _ in enumerate(word):
        wordData.append("_")
    wordData = info_adder(wordData, guessedLetters)
    print(" ".join(wordData)) # Prints the list with each character seperated by a space
    print(f"You have {guessCount} wrong guesses left")


def win_checker(word, guessedLetters):
    """Checks if game has been won."""
    correctLetters = 0
    for letter in enumerate(word):
        # If a letter in word is in guessedLetters, that means it has been correctly guessed, so incremeant the counter
        if letter[1] in guessedLetters:
            correctLetters += 1
    if correctLetters == len(word):
        return True
    return False


guessReset = 8 # What the guessCount is reset to
while True:
    # Initialize's the varibles
    guessCount = guessReset
    guessedLetters = []
    word = word_loader()
    word_printer(word, guessCount, guessedLetters)
    while guessCount != 0 and not win_checker(word, guessedLetters):
        guessedLetters = word_updater(guessedLetters, word)
        word_printer(word, guessCount, guessedLetters)
    print("\n")
    if win_checker(word, guessedLetters):
        print("You won!")
        guessReset = guessReset - 1 # Decreases guessCount on a win to increase difficulty
    else:
        print(f"You lost! The word was {word}")
        guessReset += 1 # Increases guessCount on a loss to decrease difficulty
    if input("Would you like to play again? (y/n)").lower() == "n":
        break
    print("\n")
