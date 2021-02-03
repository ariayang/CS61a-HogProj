# CS61a-HogProj

In Hog, two players alternate turns trying to be the first to end a turn with at least 100 total points. On each turn, the current player chooses some number of dice to roll, up to 10. That player's score for the turn is the sum of the dice outcomes. However, a player who rolls too many dice risks:

Sow Sad. If any of the dice outcomes is a 1, the current player's score for the turn is 1.

In a normal game of Hog, those are all the rules. To spice up the game, we'll include some special rules:

Piggy Points. A player who chooses to roll zero dice scores k+3 points, where k is the digit in the squared opponent’s score that has the lowest value.

More Boar. First, the points for the turn are added to the current player’s score. Then the current player takes another turn if the leftmost digit of the current player's score is smaller than the leftmost digit of the opponent's score and the second leftmost digit of the current player's score is smaller than the second leftmost digit of the opponent's score. If either score is only a singular digit, assume it has a 0 in front of it (e.g. 1 -> 01, 6 -> 06). You may not assume that the scores are under 100. The More Boar calculation should be done on the current player's score after the points from the current turn are added.

Only changes needed to be changed is hog.py 

Starter files:
  hog.py: A starter implementation of Hog
  dice.py: Functions for rolling dice
  hog_gui.py: A graphical user interface (GUI) for Hog
  ucb.py: Utility functions for CS 61A
  ok: CS 61A autograder
  tests: A directory of tests used by ok
  gui_files: A directory of various things used by the web GUI
