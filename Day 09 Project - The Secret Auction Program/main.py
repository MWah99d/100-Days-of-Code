from art import logo


def auction(bidders):
    highest_bid = 0
    for key in bidders:
        if bidders[key] > highest_bid:
            winner = key
            highest_bid = bidders[key]
    print(f"The winner is {winner}, with a bid of ${highest_bid}")


print(logo)
print("Welcome to the secret auction program.")
all_bidders = {}
should_continue = True
while should_continue:
    bidder = input("What's your name? ")
    bid = int(input("What's your bid?: $"))
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    all_bidders[bidder] = bid
    if other_bidder == "no":
        should_continue = False
auction(all_bidders)
