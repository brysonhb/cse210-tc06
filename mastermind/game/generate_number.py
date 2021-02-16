import random
from game.roster import Roster


class GenerateNumber:

    def __init__(self):
        """
        The constructor method.
        """
        self.roster = Roster()
        self._number = 0
        self.guess = ''
        self.random_number = 0
        self.guess1 = '----'
        self.guess2 = '----'
        self.guesses = []

    def set_number(self):
        """
        The set_number method sets a number range and returns a random choice in
        that range.
        """
        self._number = range(1000, 9999)
        self.random_number = random.choice(self._number)
        return str(self.random_number)

    def get_number(self):
        """
        The get_number method gets the value from set_number and returns the value
        and sends it to screen.
        """
        return self.random_number

    def get_guess(self, player):
        """
        The get_guess method prompts the user to input their guess and returns that
        value to screen.
        """
        print(f"{player}'s turn:")
        guess = str(input("What is your guess? "))
        print()
        return guess
