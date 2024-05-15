import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'computer', 'code','codealpha','intern','orange','teacher']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts_left = 10

    print("Welcome to Hangman!")
    
    while True:
        print("\nAttempts left:", attempts_left)
        print("Word:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        elif guess not in word:
            attempts_left -= 1
            print("Incorrect guess!")
            if attempts_left == 0:
                print("You ran out of attempts. The word was:", word)
                break
        else:
            print("Correct guess!")
        
        guessed_letters.append(guess)
        
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

if __name__ == "__main__":
    hangman()
