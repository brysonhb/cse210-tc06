from game.roster import Roster

class Board:

    def __init__(self):
        """
        The constructor of the Board class
        """
        self.roster = Roster()
        self._spacer = '--------------------\n'
        self._p1_guess = '----'
        self._p2_guess = '----'


        pass

    def to_string(self):
        """
        Formats the content to a string so that it can be displayed on the screen without issue
        Takes the names from the Roster class as arguments
        :return: string
        """
        string = self._spacer + "Player " + self.roster.get_P1() + ': ' + self._p1_guess + ', '
        string +=

        pass

    def print_guesses(self):
        """
        ?
        :return:
        """
        pass

    def print_num_condition(self):
        """
        ?
        :return:
        """
        pass