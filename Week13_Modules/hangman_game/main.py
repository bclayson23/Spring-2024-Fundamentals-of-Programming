import random
from hangman_ascii import stages, logo
from words import words

# Take a list with sample words
# words1 = ["sunrise", "mountain", "forest", "beach"]
play_again = "yes"
while play_again in ["yes", "y"]:
    # Choose a random word
    chosen_word = random.choice(words)
    len_chosen_word = len(chosen_word)
    # print(chosen_word)
    print(logo)
    # Create a list with as many dashes as there are letters in the word
    word_display = []
    for _ in range(len_chosen_word):
        word_display.append("_")

    # print(word_display)
    print(stages[7])
    print(word_display)

    # Take a flag to keep track of game result
    game_over = False
    # Take a counter to keep track of life count
    lives_left = 7
    # To keep track of incorrectly guessed letters
    incorrect_guessed_letters = []

    while not game_over:
        guessed_letter = input("Guess a letter: ").lower()

        if guessed_letter in word_display or guessed_letter in incorrect_guessed_letters:
            print(f"You have already guessed {guessed_letter}. Try again!")
            print(f"Number of lives left: {lives_left}")

        elif guessed_letter not in chosen_word:
            print(f"Your guess, {guessed_letter}, is not in the word. You lose a life")
            lives_left -= 1
            print(f"Number of lives left: {lives_left}")
            incorrect_guessed_letters.append(guessed_letter)
            if lives_left == 0:
                game_over = True
                print("Game Over! You Lose!")
                print(f"The word was {chosen_word}")

        else:
            for idx, val in enumerate(chosen_word):
                if val == guessed_letter:
                    word_display[idx] = guessed_letter
            print(f"Number of lives left: {lives_left}")

        # print(word_display)
        print(stages[lives_left])
        print(word_display)

        if "_" not in word_display:
            game_over = True
            print("You Win!")

    play_again = input("Do you want to play again? Enter yes or y ").lower()
