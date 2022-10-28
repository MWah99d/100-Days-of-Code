import random
from art import logo, vs
from game_data import data


def compare():
    if account_a['follower_count'] > account_b['follower_count']:
        return account_a['follower_count']
    else:
        return account_b['follower_count']


def get_answer_followers():
    if guess == "a":
        return account_a['follower_count']
    else:
        return account_b['follower_count']


def check_answer(total_score):
    if get_answer_followers() == compare():
        total_score += 1
        print(f"You're right! Current score: {total_score}")
        return total_score
    else:
        print(f"Sorry, that's wrong. Final score: {total_score}")
        return -1


print(logo)
score = 0
account_a = random.choice(data)
while score != -1:
    account_b = random.choice(data)
    while account_b == account_a:
        account_b = random.choice(data)
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
    print(vs)
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")
    guess = input("Who has more follower? Type 'A' or 'B': ").lower()
    score = check_answer(score)
    account_a = account_b
