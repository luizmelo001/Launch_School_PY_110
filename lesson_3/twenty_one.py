"""A simple implementation of the Blackjack (Twenty-One) card game."""
import random
import os

DEALER_LIMIT = 17
GAME_LIMIT = 21
SUITS = ['H', 'D', 'C', 'S']
CARD_POINTS = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11  
}

def clear_screen():
    """Clears the console screen based on the operating system."""
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def shuffle(cards):
    """Shuffles the given list of cards in place."""
    random.shuffle(cards)

def initialize_deck():
    """Creates and shuffles a standard 52-card deck."""
    values = [str(val) for val in range(2,11)] + ['Jack', 'Queen', 'King', 'Ace']
    deck = []

    for value in values:
        for suit in SUITS:
            deck.append([value, suit])

    shuffle(deck)
    return deck

def prompt(message):
    """Prints a message with a '=>' prefix."""
    print(f"=> {message}")

def draw_card(deck, num_cards):
    """Draws the specified number of cards from the deck."""
    return [deck.pop(0) for _ in range(num_cards)]

def calculate_total(hand):
    """Calculates the total value of a hand, adjusting Aces as needed."""
    total = 0
    aces = 0

    # Step 1: Add non-Ace cards and count Aces
    for card in hand:
        if card[0] == 'Ace':
            aces += 1
            total += 11
        else:
            total += CARD_POINTS[card[0]]

    while total > GAME_LIMIT and aces > 0:
        total -= 10 # Reduce an Ace from 11 to 1
        aces -= 1

    return total

def busted(hand):
    """Checks if the hand's total exceeds the game limit."""
    return calculate_total(hand) > GAME_LIMIT

def format_cards(hand):
    """Formats a hand of cards as a string."""
    return ', '.join(f"{card[0]} {card[1]}" for card in hand)

def player_status(player_hand):
    """Displays the player's current hand and total."""
    prompt(f"Your hand: {format_cards(player_hand)} (Total: {calculate_total(player_hand)})")

def player_turn(hand, deck):
    """Manages the player's turn, allowing hit or stay."""
    player_status(hand)
    while True:
        answer = input("Would you like to (h)it or (s)tay? ").lower()
        if answer == 's':
            break

        if answer == 'h':
            new_card = draw_card(deck, 1)
            hand += new_card
            prompt(f"You drew {new_card[0][0]} {new_card[0][1]}")
            player_status(hand)
            if calculate_total(hand) > GAME_LIMIT:
                break
        else:
            prompt("Sorry, must enter 'h' or 's'.")
    return hand

def dealer_turn(hand, deck):
    """Manages the dealer's turn, hitting until at least DEALER_LIMIT."""
    dealer_total = calculate_total(hand)

    while dealer_total < DEALER_LIMIT:
        prompt(f"Dealer hand: {format_cards(hand)} (Total: {dealer_total})")
        new_card = draw_card(deck, 1)
        hand += new_card
        dealer_total = calculate_total(hand)
        prompt(f"Dealer drew {new_card[0][0]} {new_card[0][1]} (New total: {dealer_total})")
        if busted(hand):
            prompt("Dealer busted!")
            break
    return hand

def display_results(player_cards, dealer_cards):
    """Displays the results of a round and determines the winner."""
    player_total = calculate_total(player_cards)
    dealer_total = calculate_total(dealer_cards)

    prompt(
        f"Your hand: {format_cards(player_cards)}"
        f"(Total: {player_total})"
    )
    prompt(
        f"Dealer's hand: {format_cards(dealer_cards)}"
        f"(Total: {dealer_total})"
    )

    if busted(player_cards):
        prompt("Dealer wins!")
        return "dealer"

    if busted(dealer_cards):
        prompt("You win!")
        return "player"

    if player_total > dealer_total:
        prompt("You win!")
        return "player"

    if dealer_total > player_total:
        prompt("Dealer wins!")
        return "dealer"

    prompt("It's a tie.")
    return 'tie'

def display_score(player, dealer):
    """Displays the current score of the player and dealer."""
    print('==============')
    prompt("Total score:")
    prompt(f"Player: {player}  /  Dealer: {dealer}")
    print('==============')

def validate_input(message, valid_options):
    """Validates user input against a list of valid options."""
    while True:
        choice = input(message).lower().strip()
        if (choice in valid_options
            or choice.startswith(valid_options[0])
            or choice.startswith(valid_options[1])):
            return choice.startswith(valid_options[0])
        prompt(f"Please enter {valid_options[0]} or {valid_options[1]}")


def play_again():
    """Asks if the user wants to play another round."""
    answer = validate_input("Would you like to play again? yes or no ", ['y', 'n'])

    return answer in ('y', 'yes')

def play_twenty_one():
    """Runs the main game loop for Twenty-One."""
    player_score = 0
    dealer_score = 0

    while player_score < 3 and dealer_score < 3:
        clear_screen()
        deck = initialize_deck()
        player_hand = draw_card(deck, 2)
        dealer_hand = draw_card(deck, 2)
        display_score(player_score, dealer_score)

        # Player's turn
        prompt(f"Dealer shows: {dealer_hand[0][0]} {dealer_hand[0][1]} and unknown card")

        player_turn(player_hand, deck)
        if busted(player_hand):
            dealer_score += 1
            display_results(player_hand, dealer_hand)
            if play_again():
                continue
            break

        # Dealer's turn (hit until >= 17)
        dealer_turn(dealer_hand, deck)
        if busted(dealer_hand):
            player_score += 1
            display_results(player_hand, dealer_hand)
            if play_again():
                continue
            break

        # Compare totals
        winner = display_results(player_hand, dealer_hand)
        if winner == 'player':
            player_score += 1

        if winner == 'dealer':
            dealer_score += 1

        if not play_again():
            break

    if player_score >= 3:
        prompt("Player wins the match!")

    if dealer_score >= 3:
        prompt("Dealer wins the match!")
        prompt("Thank you for playing!")

play_twenty_one()
