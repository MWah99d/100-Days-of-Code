import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)

display = []
display += "_" * len(chosen_word)

lives = 6
print(logo)
print(f'Pssst, the solution is {chosen_word}.')

while "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    elif guess not in chosen_word:
        lives -= 1
        print(f"Letter {guess} is not in the word.")
    else:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess

    print(f"{' '.join(display)}")
    print(stages[lives])

    if lives == 0:
        print("You lose.")
        break

    if "_" not in display:
        print("You win.")
        break
