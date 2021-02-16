class Roster:

    def __init__(self):
        """
        The constructor method.
        """
        self._players = []

    def set_name(self):
        """
        The get_name method simply asks the players to input their names
        and then returns that value to screen.
        """
        player1 = input('Enter a name for player 1: ')
        self._players.append(player1)
        player2 = input('Enter a name for player 2: ')
        self._players.append(player2)
        print()
        return self._players
