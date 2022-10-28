from random import randint
from art import logo


def guess_the_number(total_attempts, correct_answer):
    print(f"You have {total_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == correct_answer:
        print(f"You got it, the answer was {correct_answer}.")
    else:
        total_attempts -= 1
        if total_attempts == 0:
            print("Wrong answers.\nYou've run out of guesses, You lose.")
        else:
            if guess > correct_answer:
                print("Too high\nGuess again.")
            else:
                print("Too low\nGuess again.")
            guess_the_number(total_attempts, correct_answer)


print(logo)
print("Welcome to the Number Guessing Game!")
random_number = randint(1, 100)
attempts = 5
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {random_number}.")
difficulty = input("Choose the difficulty, Type 'easy' or 'hard'. ").lower()
if difficulty == "easy":
    attempts = 10
guess_the_number(attempts, random_number)
