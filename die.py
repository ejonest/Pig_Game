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
"""This module creates the Die class and defines what it does"""
from random import randrange


# This could be a function but was made as a class to demenstrate how
# to do that
class Die:
    """This is the Die class. It performs the function of a die being rolled"""
    def __init__(self):
        pass

    def roll(self):
        """Roll simulates rolling a die"""
        return randrange(1, 7)


if __name__ == "__main__":
    D = Die()
    for i in range(10):
        print(D.roll())
