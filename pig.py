#!/usr/bin/env python3
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
"""This module is the one that ties everything together and is the one run in
    the terminal."""
import game

if __name__ == "__main__":
    GAME = game.PigGame()
    GAME.run()
