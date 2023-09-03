from src.services.match_score_calculation_service.match_score_logic.player_score import PlayerScore
from src.services.match_score_calculation_service.match_score_logic.tennis_score import TennisScore


class WrumWrumLogic:
    def __init__(self):
        self.player_1 = PlayerScore()
        self.player_2 = PlayerScore()

        score_up = TennisScore(self.player_1, self.player_2)

        while True:
            num = int(input("Введите 1, 2 или 3 "))

            if num == 1:
                score_up.player1_count_score()
                print(score_up.current_account())
            elif num == 2:
                score_up.player2_count_score()
                print(score_up.current_account())
            elif num == 3:
                print(score_up.current_account())
                print('До скорого!')
                break


if __name__ == '__main__':
    wrum = WrumWrumLogic()
