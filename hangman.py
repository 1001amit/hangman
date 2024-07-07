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

def print_hangman(attempts_left, max_attempts):
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
        ''',
        '''
           ------
           |    |
           |    O1
           |   /|\\
           |   / \\
           |
        ------
        ''','''
           ------
           |    |
           |    O2
           |   /|\\
           |   / \\
           |
        ------
        ''','''
           ------
           |    |
           |    O3
           |   /|\\
           |   / \\
           |
        ------
        ''','''
           ------
           |    |
           |    O4
           |   /|\\
           |   / \\
           |
        ------
        '''
    ]
    stage_index = max_attempts - attempts_left
    print(hangman_stages[stage_index])

def choose_difficulty():
    print("Choose a difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def play_round(max_attempts):
    word = fetch_random_word()
    if word is None:
        print("Failed to fetch a random word. Please try again.")
        return False

    guessed_letters = []
    attempts_left = max_attempts
    game_over = False

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    print_hangman(attempts_left, max_attempts)

    while not game_over:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            attempts_left -= 1
            print("Wrong guess. Attempts left:", attempts_left)

        print(display_word(word, guessed_letters))
        print_hangman(attempts_left, max_attempts)

        if '_' not in display_word(word, guessed_letters):
            game_over = True
            print("Congratulations, you won!")
            return True
        elif attempts_left == 0:
            game_over = True
            print("Sorry, you lost. The word was:", word)
            return False

def hangman():
    max_attempts = choose_difficulty()
    rounds = 0
    wins = 0
    losses = 0

    while True:
        result = play_round(max_attempts)
        rounds += 1
        if result:
            wins += 1
        else:
            losses += 1

        print(f"Rounds played: {rounds}")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    hangman()
