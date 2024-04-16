import random  # importing the random module
from hangman_ascii import stages, logo  # im[porting ascii art
from words import words, words_alpha  # importing the words

# Take a list with sample words
# words1 = ["sunrise", "mountain", "forest", "beach"]

# Debugging, with breakpoints, program stops at point
play_again = "yes"  # to play again
while play_again in ["yes", "y"]:  # setting to play
    # Choose a random word
    chosen_word = random.choice(words_alpha)  # calling for words
    len_chosen_word = len(chosen_word)  # finding word length
    # print(chosen_word)
    print(logo)  # printing the logo
    # Create a list with as many dashes as there are letters in the word
    word_display = []  # place holder
    for _ in range(len_chosen_word):  # displaying the blanks
        word_display.append("_")

    # print(word_display)
    print(stages[7])  # for the stages and the word
    print(word_display)

    # Take a flag to keep track of game result
    game_over = False
    # Take a counter to keep track of life count
    lives_left = 7
    # To keep track of incorrectly guessed letters
    incorrect_guessed_letters = []

    while not game_over:  # for the game duration
        guessed_letter = input("Guess a letter: ").lower()  # user input of guess

        if guessed_letter in word_display or guessed_letter in incorrect_guessed_letters:  # for already guessed letter
            print(f"You have already guessed {guessed_letter}. Try again!")
            print(f"Number of lives left: {lives_left}")

        elif guessed_letter not in chosen_word:  # for a bad guess
            print(f"Your guess, {guessed_letter}, is not in the word. You lose a life")
            lives_left -= 1  # to take a life away
            print(f"Number of lives left: {lives_left}")
            incorrect_guessed_letters.append(guessed_letter)
            if lives_left == 0:  # checking for no lives
                game_over = True
                print("Game Over! You Lose!")  # for game over
                print(f"The word was {chosen_word}")

        else:  # for a successful guess
            for idx, val in enumerate(chosen_word):
                if val == guessed_letter:  # to display the letter in place
                    word_display[idx] = guessed_letter
            print(f"Number of lives left: {lives_left}")

        # print(word_display)
        print(stages[lives_left])  # printing stage image
        print(word_display)  # printing the word display

        if "_" not in word_display:  # checking for fully guessed word
            game_over = True
            print("You Win!")

    play_again = input("Do you want to play again? Enter yes or y ").lower()  # asking to replay
