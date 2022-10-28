import random
from art import logo


def get_score(cards_list):
    if sum(cards_list) > 21 and 11 in cards_list:
        cards_list.remove(11)
        cards_list.append(1)
        return sum(cards_list)
    else:
        return sum(cards_list)


def get_another_card():
    global user_score
    while user_score < 21:
        another_card = input("Do you want to get another card, Type 'yes' or 'no': ").lower()
        if another_card == "yes":
            user_cards.append(random.choice(cards))
            user_score = get_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            get_another_card()
        break


def add_card():
    global computer_score
    while computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = get_score(computer_cards)


def get_the_winner():
    print("-----------------------------------------------------------------------------")
    print(f"Your hand: {user_cards}, Score: {user_score}.\nComputer's hand: {computer_cards}, Score: {computer_score}.")
    if user_score > 21:
        print("Bust, You lose.")
    elif user_score == computer_score:
        print("It's a draw")
    elif user_score == 21:
        print("Blackjack, You win.")
    elif computer_score > 21:
        print("Bust, You win.")
    elif user_score > computer_score:
        print("You win.")
    else:
        print("You lose.")


print(logo)
print("Welcome to Blackjack Game")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = [random.choice(cards), random.choice(cards)]
user_score = get_score(user_cards)
computer_cards = [random.choice(cards), random.choice(cards)]
computer_score = get_score(computer_cards)
add_card()
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {computer_cards[0]}")
get_another_card()
get_the_winner()
