
import hangman_words
import random
from hangman_art import stages
from hangman_art import logo

def cls():
    print('\n' * 50)
print(logo)
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# Testing code
# print(f'Pssst, the solution is {chosen_word}.')
display = []
for letter in chosen_word:
    display += "_"

end_of_game = False

lives = 6
guess_list = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    cls()
    if guess in guess_list:
        print("You already used that letter, try again.")
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = guess
        if guess not in chosen_word:
            print(f"The letter: {guess} is not in the word.")
            lives -= 1
        print(stages[lives])
        print(f"{' '.join(display)}")
        print(f"Lives left: {lives}")

        if "_" not in display:
            end_of_game = True
            print("You win!")
        if lives <= 0:
            print("You Lose.")
    for gues in guess:
        guess_list += guess
    # print(guess_list)
