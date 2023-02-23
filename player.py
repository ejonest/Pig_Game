# Ethan Jones
# CPSC 386-04
# 2022-03-01
# ejonest@csu.fullerton.edu
# @ejonest
#
# Lab 04-00
#
# This is our first python game. It is pig and it plays until a player gets 30
#
"""This is module holds the Player class and CompPlayer class.\
    They designate names and creates getters, setters,\
    and important functions for the game to run"""


class Player:
    """Player class defines the player, its members, and its funtions"""
    def __init__(self, name, order):
        # The _ is to tell other programmers don't mess with this
        self._name = name
        self._score = 0
        self._order = order

    # getters
    def name(self):
        """getter for name"""
        return self._name

    def order(self):
        """getter for order"""
        return self._order

    def score(self):
        """getter for score"""
        return self._score

    def am_i_human(self):
        """returns true for being a human for player"""
        return True

    def are_you_real(self):
        """This returns a string saying the player is human"""
        return "Yes, I am a regular human bar tender."

    # This one is used to get the name and __str__ denotes it as a string
    def __str__(self):
        return self._name

    def __repr__(self):
        return "({}) {} points".format(self._name, self._score)

    # setters
    def score(self, new_score):
        """setter for score"""
        self._score = new_score

    def order(self, order):
        """setter for order"""
        self._order = order


class CompPlayer(Player):
    """class for the computer player it is a subclass of Player"""
    def __init__(self, order, game):
        super().__init__("Aida", order)
        self._game = game
        self._score = 0

    # marks the computer as not am_i_human
    def am_i_human(self):
        return False

    # This is a way to check if the player is human or not
    def are_you_real(self):
        return self._game.am_i_real()

    def does_roll(self):
        opponent_score = self._game.opponent_score(self)
        if opponent_score > 12:
            return True
        else:
            return False
        # if op_score > 26:
        # return True
        # elif self._score == 0:
        # return True
        # elif (op_score - self._score) > 20:
        # return True
        # elif randrange(1,3) == 1:
        # return True
        # else:
        # return False
