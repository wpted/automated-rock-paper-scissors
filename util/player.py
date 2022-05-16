from random import choice


class Player:
    def __init__(self):
        self.decision_list = ["Rock", "Paper", "Scissors"]
        self.wins = 0
        self.loses = 0

    def choose(self) -> str:
        return choice(self.decision_list)
