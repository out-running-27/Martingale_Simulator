# This program is designed to recreate the Martingale style of betting and prove a long dispute with a
# friend of mine that it will not work The Martingale system is simple, take a near 50/50 bet,
# we will be simulating Red/Black in roulette, if you lose simply double your bet.
# So, starting at $10 dollars, if the player loses, your next bet would be $20, then $40, and growing
# exponentially, until the player wins. At this point the player would place another bet of $10 and begin again

import random


def play_roulette(color):
    """
    "You have to play to win'
    Input: the color (Red or Black) which the player is betting on
    Output: True if the player wins, False indicates a loss
    """

    wheel = {
        "red": [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
        "black": [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
        "green": [0, -1]}  # -1 is used to simulate 00, -1 or 0 are a guaranteed loss when betting red/black

    ball = random.randint(-1, 37)  # Where is the ball going to land?!

    if ball in wheel[color]:  # did the ball number match the color of the bet?
        return True  # winner!
    else:
        return False  # loser :(

def calculate_bet(starting_bet, losing_streak, life_savings):

    bet = starting_bet * (2**losing_streak)         # bet grows exponentially to losing streak

    if bet > life_savings:                          # we don't allow credit at this casino
        bet = life_savings
    return bet


def play_game():
    """
    The player will get to signify the starting cash,
    :return:
    """

    print("Welcome to the Martingale Simulator!")
    starting_bet = int(input("How much would you like your starting bet to be?: "))
    life_savings = int(input("What is your current life savings? Don't worry, there's only a very small chance "
                             "you'll lose it all: "))
    color = input("Which color would you like to bet on? (black/red): ").lower()
    # desired_winnings = int(input("How much money would you like to win?: "))

    game_number = 0
    losing_streak = 0
    current_bet = starting_bet
    largest_bet = starting_bet

    while life_savings > 0:
        current_bet = calculate_bet(starting_bet, losing_streak, life_savings)

        if current_bet > largest_bet:
            largest_bet = current_bet
        if play_roulette(color):  # You win!
            life_savings += current_bet
            losing_streak = 0
        else:  # You lost
            life_savings -= current_bet
            losing_streak += 1

        game_number += 1

        if game_number % 10000 == 0:
            print("round number {}; life savings {}; largest bet so far: {}".format(
                game_number, life_savings, largest_bet))

    print("Oh no you lost it all on round {}, with a bet of ${} "
          "after a losing streak of {}, the largest bet you made was ${}"
          .format(game_number, current_bet, losing_streak, largest_bet))


play_game()
