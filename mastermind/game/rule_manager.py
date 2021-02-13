
class Rule_manager:
    
    def __init__(self):
        self.hint = '****'
        self.num_turn = -1
    
    
    def _get_hint(self, number, guess):
        """
        check if the guessed number is in the number
        return hint: "****"
        """
        list_num = []
        
        for i in range(4):
            list_num.append(number[i:i+1])
        
        for i in range(4):
            for j in range(4):
                if guess[i:i+1] == list_num[j]:
                    if i == j:
                        self.hint[i:i+1] = 'x'
                    else:
                        self.hint[i:i+1] = 'o'
        return self.hint

    def _game_over(self, number, guess):
        """
        If the guessed number is correct, return False
        """

        if guess == number:
            return False
        
        return True

    def next_player(self):
        """
        If Ture, player 1's turn 
        False, player 2's turn
        """
        self.num_turn += 1
        if self.num_turn % 2 == 0:
            return True
        
        return False



