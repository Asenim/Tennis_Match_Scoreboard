from src.services.match_score_calculation_service.match_score_logic.player_score import PlayerScore
from src.services.match_score_calculation_service.match_score_logic.tennis_game_score import TennisGameScore
from src.services.match_score_calculation_service.match_score_logic.tennis_set_score import TennisSetScore
from src.services.match_score_calculation_service.match_score_logic.tennis_tiebreak_score import TieBreakScore


class WrumWrumLogic:
    def __init__(self, player1_name, player2_name):
        """Класс запускает логику приложения"""
        self.player_1 = PlayerScore(player1_name)
        self.player_2 = PlayerScore(player2_name)

        game_score_up = TennisGameScore(self.player_1, self.player_2)
        set_score_up = TennisSetScore(self.player_1, self.player_2)

        while True:
            if self.player_1.game == 6 and self.player_2.game == 6:
                self.__tie_break_wrum_wrum()

            num = input("Вы в зоне счета Введите 1, 2 или 3 ")

            if num == '1':
                game_score_up.player1_count_score()
                set_score_up.player1_set_win()
                self.player_1.player_all_score_get()
            elif num == '2':
                game_score_up.player2_count_score()
                set_score_up.player2_set_win()
                self.player_2.player_all_score_get()

            elif self.player_1.game_set == 3:
                print("Игрок 1 выиграл матч")
                break

            elif self.player_2.game_set == 3:
                print("Игрок 2 выиграл матч")
                break

            elif num == '3':
                print('До скорого!')
                break

    def __tie_break_wrum_wrum(self):
        tie_break_score = TieBreakScore(self.player_1, self.player_2)

        set_score1 = self.player_1.game_set
        set_score2 = self.player_2.game_set

        while True:
            if set_score1 + 1 == self.player_1.game_set:
                break
            if set_score2 + 1 == self.player_2.game_set:
                break

            print("Начинается тай-брейк!")
            print("Вам так же нужно будет вводить 1, 2 или 3")

            num = input("Введите 1 или 2 ")

            if num == '1':
                tie_break_score.player1_tie_break_win()
                self.player_1.player_all_score_get()
            elif num == '2':
                tie_break_score.player2_tie_break_win()
                self.player_2.player_all_score_get()


if __name__ == '__main__':
    wrum = WrumWrumLogic('Sergey', "Alfob")
