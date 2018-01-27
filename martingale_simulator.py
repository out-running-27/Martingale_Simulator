
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
            "green": [0, -1]}       # -1 is used to simulate 00, -1 or 0 are a guaranteed loss

    ball = random.randint(-1, 37)   # Where is the ball going to land?!

    if ball in wheel[color]:        # did the ball number match the color of the bet?
        return True                 # winner!
    else:
        return False                # loser :(



