import random
import requests

def fetch_random_word():
    response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    if response.status_code == 200:
        return response.json()[0]
    else:
        return None

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def print_hangman(attempts):
    hangman_stages = [
        '''
           ------
           |    |
           |
           |
           |
           |
        ------
        ''',
        '''
           ------
           |    |
           |    O
           |
           |
           |
        ------
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |
           |
        ------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |
           |
        ------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        ------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        ------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ------
        '''
    ]
    print(hangman_stages[6 - attempts])

def hangman():
    word = fetch_random_word()
    if word is None:
        print("Failed to fetch a random word. Please try again.")
        return

    guessed_letters = []
    attempts = 6
    game_over = False

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    print_hangman(attempts)

    while not game_over:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Wrong guess. Attempts left:", attempts)

        print(display_word(word, guessed_letters))
        print_hangman(attempts)

        if '_' not in display_word(word, guessed_letters):
            game_over = True
            print("Congratulations, you won!")
        elif attempts == 0:
            game_over = True
            print("Sorry, you lost. The word was:", word)

if __name__ == "__main__":
    hangman()
