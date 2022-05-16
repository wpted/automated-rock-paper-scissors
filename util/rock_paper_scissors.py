from util.player import Player


class RockPaperScissors:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.draws = 0

    def count_wins(self):
        player1_result = self.player1.choose()
        player2_result = self.player2.choose()

        def draw():
            if player1_result == player2_result:
                self.draws += 1

        if player1_result == "Rock":
            if player2_result == "Paper":
                self.player1.loses += 1
                self.player2.wins += 1

            elif player2_result == "Scissors":
                self.player1.wins += 1
                self.player2.loses += 1
            else:
                draw()

        elif player1_result == "Paper":
            if player2_result == "Scissors":
                self.player1.loses += 1
                self.player2.wins += 1

            elif player2_result == "Rock":
                self.player1.wins += 1
                self.player2.loses += 1
            else:
                draw()

        elif player1_result == "Scissors":
            if player2_result == "Rock":
                self.player1.loses += 1
                self.player2.wins += 1

            elif player2_result == "Paper":
                self.player1.wins += 1
                self.player2.loses += 1
            else:
                draw()
