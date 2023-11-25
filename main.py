# Black Jack Game Version 0.1

# Importing the 'art' module for the game logo
from logo import art
import os
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "PUSH 😜"
    elif computer_score == 0:
        return "User LOST, Computer got BlackJack 😱"
    elif user_score == 0:
        return "You WIN, you got BlackJack 🤩"
    elif user_score > 21:
        return "You went over 21. You LOST 🤨"
    elif computer_score > 21:
        return "Computer over 21. You WIN 🥳"
    elif user_score > computer_score:
        return "You WON 🤑"
    else:
        return "You LOST 😤"

def play_game():
    print(art)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # You can use a loop for card dealing to make the code more concise.
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your Cards: {user_cards};      Current Score: {user_score}")
        print(f"    Computer's First Card: {computer_cards[0]}\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card; or 'n' to pass:  ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your deck: {user_cards};       Your Score: {user_score}\n")
    print(f"    Computer's deck: {computer_cards};       Your Score: {computer_score}\n")
    print(compare(user_score, computer_score), "\n")

# Checking if the user wants to play again, using a more informative prompt
while input("Do you want to play Blackjack? Type 'y' for yes or 'n' for no: ").lower() == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()

# END OF CODE
