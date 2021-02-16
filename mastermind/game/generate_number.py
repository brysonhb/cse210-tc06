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
        # self.player1 = self.roster.player1
        # self.player2 = self.roster.player2
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
        # self.roster.set_name(self.player1, self.player2)
        # self.guess1 = input(int(f'{self.player1} What is your guess? '))
        # self.guess2 = input(int(f'{self.player2} What is your guess? '))
        print(f"{player}'s turn:")
        guess = str(input("What is your gguess? "))
        print()
        return guess

        # return self.guess1 and self.guess2

    def guess_call_1(self):
        """
        This method just returns the value of guess 1.
        """
        return self.guess1

    def guess_call_2(self):
        """
        This method just returns the value of guess 2.
        """
        return self.guess2
