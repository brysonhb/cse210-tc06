class Board:

    def __init__(self):
        """
        The constructor of the Board class
        """
        self._spacer = '--------------------\n'


        pass

    def to_string(self, p1_name, p2_name, p1_guess, p2_guess, p1_hint, p2_hint):
        """
        Formats the content to a string so that it can be displayed on the screen without issue
        Takes the names from the Roster class as arguments
        :return: string
        """
        string = self._spacer + "Player " + p1_name + ': ' + p1_guess + ', ' + p1_hint + '\n'
        string += "Player " + p2_name + ': ' + p2_guess + ', ' + p2_hint + '\n' + self._spacer
        return string

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