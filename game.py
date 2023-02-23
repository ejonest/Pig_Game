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
"""This is module is the game module that is responsible for looping through
    the players, prompting input, and deciding a winner."""

import time
import sys
from random import randrange
from die import Die
from player import Player, CompPlayer


def help_sort(self):
    """aids in sorting the players"""
    return [self._order]


def print_slow(string):
    """used to print the text char by char slowly so it is more readable"""
    for count_x in string:
        sys.stdout.write(count_x)
        sys.stdout.flush()
        time.sleep(0.08)
    return " "


class PigGame:
    """PigGame class is the one defines all rules and is where the bulk\
        of functions lie"""
    def __init__(self):
        self._players = []

    def opponent_score(self, player_me):
        """Gets opponents score and returns it"""
        for player in self._players:
            if player_me != player:
                return player.score
        return 0

    def help_sort(self):
        """This helps to sort the order of the players"""
        return [self._order]

    def run(self):
        """This is what pig.py runs to make the game go"""
        d_die = Die()
        num_players = int(
            input(print_slow("How many people would like to play? [1-4]"))
        )
        if num_players > 4 or num_players < 0:
            print("This game can only be played with 1 to 4 players")
            num_players = int(
                input(print_slow("How many people would like to play? [1-4]"))
            )
        if num_players == 1:
            username = input(print_slow("What's your name?"))
            order = d_die.roll()
            self._players.append(Player(username, order))
            order = d_die.roll()
            self._players.append(CompPlayer(order, self))
            self._players[0].score = 0

        else:
            count = num_players
            while count > 0:
                username = input(print_slow("What's your name?"))
                order = d_die.roll()
                self._players.append(Player(username, order))
                count -= 1
        curr_index = 0
        game_state = True
        self._players.sort(key=help_sort, reverse=True)
        for count_x in self._players:
            count_x.score = 0
        while game_state:
            curr_player = self._players[curr_index]
            again = True
            if curr_player.am_i_human():
                # run the human version
                curr_score = 0
                num_rolls = 0
                while again:
                    print()
                    temp_string = "Scores: "
                    for count_x in self._players:
                        temp_string += count_x._name + ": "
                        temp_string += str(count_x.score) + " "
                    print_slow(temp_string)
                    print()
                    print_slow("{} is up".format(curr_player._name))
                    print()
                    print_slow("You're turn score is: {}".format(curr_score))
                    print()
                    print_slow("You've rolled {} times".format(num_rolls))
                    print()
                    roll_again = input(print_slow("Would you like to roll?(Y/N) "))
                    if roll_again == "Y" or roll_again == "y":
                        print_slow(str("{} is rolling again".format(
                            curr_player._name)))
                        print()
                        again = True
                        num = d_die.roll()
                        num_rolls += 1
                        if num == 1:
                            print_slow(
                                "Sorry you rolled a 1. You're turn is over")
                            print()
                            again = False
                        else:
                            print_slow("You rolled: {}".format(num))
                            print()
                            curr_score += num
                        if (curr_player.score + curr_score) >= 30:
                            curr_player.score += curr_score
                            game_state = False
                            print_slow(
                                "{} won with {} points!!!".format(
                                    curr_player._name, curr_player.score
                                )
                            )
                            print()
                            break
                    elif roll_again == "N" or roll_again == "n":
                        print_slow(
                            "Ending {}'s turn".format(curr_player._name))
                        print()
                        again = False
                        curr_player.score += curr_score
                        for count_x in self._players:
                            if count_x.score >= 30:
                                game_state = False
                                break
                    else:
                        print_slow("Invalid input. Valid inputs are(Y/N/y/n)")
                        print()
                        again = True
            else:
                # run computer version
                for player in self._players:
                    if curr_player != player:
                        op_score = player.score
                curr_score = 0
                num_rolls = 0
                while again:
                    print()
                    temp_string = "Scores: "
                    for count_x in self._players:
                        temp_string += count_x._name + ": "
                        temp_string += str(count_x.score) + " "
                    print_slow(temp_string)
                    print()
                    print_slow("{} is up".format(curr_player._name))
                    print()
                    print_slow("You're turn score is: {}".format(curr_score))
                    print()
                    if (op_score - (curr_player.score + curr_score)) > 10:
                        comp_roll_again = "Y"
                        again = True
                    if curr_player.score == 0 and curr_score == 0:
                        comp_roll_again = "Y"
                        again = True
                    elif curr_player.score < 24:
                        if randrange(1, 10) == 1:
                            comp_roll_again = "N"
                            again = False
                        else:
                            comp_roll_again = "Y"
                            again = True
                    elif curr_score > 16:
                        comp_roll_again = "N"
                        again = False
                    else:
                        if randrange(1, 3) == 1:
                            comp_roll_again = "Y"
                            again = True
                        else:
                            comp_roll_again = "N"
                            again = False
                    print_slow("You've rolled {} times".format(num_rolls))
                    print()
                    print_slow("Would you like to roll again?(Y/N) {}".format(
                        comp_roll_again))
                    print()
                    if again:
                        num = d_die.roll()
                        num_rolls += 1
                        print_slow("Rolling again")
                        print()
                        if num != 1:
                            print_slow("You rolled: {}".format(num))
                            print()
                            curr_score += num
                            if (curr_player.score + curr_score) >= 30:
                                curr_player.score += curr_score
                                game_state = False
                                print_slow(
                                    "{} won with {} points!!!".format(
                                        curr_player._name, curr_player.score
                                    )
                                )
                                print()
                                break
                        else:
                            print_slow(
                                "Sorry you rolled a 1. You're turn is over")
                            print()
                            again = False
                    else:
                        print_slow("Ending Turn")
                        print()
                        curr_player.score += curr_score
            curr_index = (curr_index + 1) % len(self._players)
