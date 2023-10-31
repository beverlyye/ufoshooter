import random
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
chosen_word = random.choice(word_list)
guesses = ""
max_attempts = 6
while max_attempts > 0:
    word_display = ""
    for letter in chosen_word:
        if letter in guesses:
            word_display += letter
        else:
            word_display += "_"

    if word_display == chosen_word:
        print("You won! The word is:", chosen_word)
        break

    print("Word:", word_display)
    print("Guesses left:", max_attempts)
    guess = input("Guess a letter: ").lower()
    
    if guess in chosen_word:
        guesses += guess
    else:
        max_attempts -= 1
        print("Incorrect guess. Try again.")

if max_attempts == 0:
    print("You ran out of guesses. The word was:", chosen_word)
