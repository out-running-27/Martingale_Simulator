# This program is designed to recreate the Martingale style of betting and prove a long dispute with a
# friend of mine that it will not work The Martingale system is simple, take a near 50/50 bet,
# we will be simulating Red/Black in roulette, if you lose simply double your bet.
# So, starting at $10 dollars, if the player loses, your next bet would be $20, then $40, and growing
# exponentially, until the player wins. At this point the player would place another bet of $10 and begin again

import random

# standard US roulette wheel
WHEEL = {
        "red": [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
        "black": [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
        "green": [0, -1]}  # -1 is used to simulate 00, -1 or 0 are a guaranteed loss when betting red/black

def play_roulette(color):
    """
    "You have to play to win'
    Input: the color (Red or Black) which the player is betting on
    Output: True if the player wins, False indicates a loss
    """

    ball = random.randint(-1, 37)  # Where is the ball going to land?!

    if ball in WHEEL[color]:  # did the ball number match the color of the bet?
        return True  # winner!
    else:
        return False  # loser :(

def play_game(starting_bet, life_savings, walk_away, color):
    """
    The player will get to signify the starting cash,
    :return:
    """
    
    game_number = 0
    losing_streak = 0
    current_bet = starting_bet
    largest_bet = starting_bet

    while life_savings > 0:

        # bet grows exponentially to losing streak
        # min, because we don't allow credit at this casino
        current_bet = min(life_savings, starting_bet * (2**losing_streak))
        largest_bet = max(current_bet, largest_bet)

        if play_roulette(color):  # You win!
            life_savings += current_bet
            losing_streak = 0
        else:  # You lost
            life_savings -= current_bet
            losing_streak += 1

        game_number += 1
        
        if life_savings > walk_away:
            print("Congradulations! You walked away in round {} "
                  "the largest bet you made this round was ${}"
                  .format(game_number, largest_bet))
            return life_savings
        # every million rounds, print out how much money they're making!
        if game_number % 100 == 0:
            print("round number {}; life savings {}; largest bet so far: {}".format(
                game_number, life_savings, largest_bet))


    print("Oh no you lost it all on round {}, with a bet of ${} "
          "after a losing streak of {}, the largest bet you made was ${}"
          .format(game_number, current_bet, losing_streak, largest_bet))

    return life_savings
def start():
    
    print("Welcome to the Martingale Simulator!")
    starting_bet = float(input("How much would you like your starting bet to be?: "))
    life_savings = float(input("What is your current life savings? Don't worry, there's only a very small chance "
                             "you'll lose it all: "))
    desired_winnings = float(input("How much money would you like to win?: "))
    color = input("Which color would you like to bet on? (black/red): ").lower()

    
    life_savings = play_game(starting_bet, life_savings, life_savings + desired_winnings, color)
    
    while life_savings != 0:
         print("Nice job your life savings is now {}".format(life_savings))
         play = input("would you like to play again? [Y/n]: ").lower()
         if play == 'n':
             break
         else:
             starting_bet = float(input("How much would you like your starting bet to be?: "))
             desired_winnings = float(input("How much money would you like to win?: "))
             color = input("Which color would you like to bet on? (black/red): ").lower()
             life_savings = play_game(starting_bet, life_savings, life_savings + desired_winnings, color)
         

start()