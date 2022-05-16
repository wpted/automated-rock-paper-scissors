from util.rock_paper_scissors import RockPaperScissors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def computer_fight():
    game_result_list = []
    game_round = 0
    for _ in range(2000):
        RPS = RockPaperScissors()
        game_round += 1
        for _ in range(10000):
            RPS.count_wins()

        game_dict = [game_round,
                     RPS.player1.wins,
                     RPS.player2.wins,
                     RPS.draws,
                     RPS.player1.wins + RPS.player2.wins + RPS.draws
                     ]

        game_result_list.append(game_dict)

    game_result_df = pd.DataFrame(np.array(game_result_list),
                                  columns=["Round", "Player_1_Wins", "Player_2_Wins", "Draws", "TotalGames"]
                                  )

    print(game_result_df)

    plt.figure(figsize=(16, 10))
    plt.xticks(fontsize=14)
    plt.xlabel("Round", fontsize=14)
    plt.yticks(fontsize=14)
    plt.ylabel("Win Times", fontsize=14)
    plt.ylim(3000, 3700)
    plt.xlim(0, 2000)

    for column in game_result_df.columns:
        plt.plot(game_result_df.index, game_result_df[column], linewidth=1, label=game_result_df[column].name)

    plt.legend(fontsize=16)
    plt.show()


if __name__ == '__main__':
    computer_fight()
