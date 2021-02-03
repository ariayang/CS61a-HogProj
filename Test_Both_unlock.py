from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact
from hog import *

def echo_0(s0=2, s1=0):
    print('*', s0)
    #return echo_0

def echo_1(s0=2, s1=2):
    print('**', s1)
    #return echo_1

def both(f, g):
    """Return a commentary function that says what f says, then what g says.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Player 0 now has 10 and Player 1 now has 0
    Player 0 takes the lead by 10
    >>> h2 = h1(10, 8)
    Player 0 now has 10 and Player 1 now has 8
    >>> h3 = h2(10, 17)
    Player 0 now has 10 and Player 1 now has 17
    Player 1 takes the lead by 7
    """
    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say

echo_0(2, 0)
echo_1(2, 2)
both(echo_0, echo_1)

### Below is to test roll_dice, average, Question 8
dice = make_test_dice(3, 1, 5, 6)
print (roll_dice(2, dice))
print (roll_dice(2, dice))
print (roll_dice(2, dice))
print (roll_dice(2, dice))
print (roll_dice(2, dice))

