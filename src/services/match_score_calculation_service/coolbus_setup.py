from src.services.match_score_calculation_service.match_score_logic.player_score import PlayerScore
from src.services.match_score_calculation_service.match_score_logic.tennis_game_score import TennisGameScore
from src.services.match_score_calculation_service.match_score_logic.tennis_set_score import TennisSetScore
from src.services.match_score_calculation_service.match_score_logic.tennis_tiebreak_score import TieBreakScore


class CoolBusSetUp:
    def __init__(self, id_match, player1_object_model, player2_object_model, player1_score, player2_score, point_win_request):
        """
        Класс запускает логику приложения
        :param id_match: id матча подсчет которого производится в данный момент
        :param player1_object_model: игрок 1 из таблицы players
        :param player2_object_model: игрок 2 из таблицы players
        :param player1_score: Текущий счет игрока 1 (берется из таблицы Matches -> Score -> player1)
        :param player2_score: Текущий счет игрока 2 (берется из таблицы Matches -> Score -> player2)
        :param point_win_request: Информация из Post запроса
        """
        self.id_match = id_match
        self.player_1 = PlayerScore(player1_object_model, score_player=player1_score)
        self.player_2 = PlayerScore(player2_object_model, score_player=player2_score)
        self.point_win_request = point_win_request

    def start_counting_score(self):
        """
        Производится непосредственно подсчет очков в матче.
        :return: Объект игрока с результатами матча
            (со всей информацией из полей класса PlayerScore)
        """
        game_score_up = TennisGameScore(self.player_1, self.player_2)
        set_score_up = TennisSetScore(self.player_1, self.player_2)

        num = self.point_win_request

        if self.player_1.game_set == 3:
            print("Игрок 1 выиграл матч")
            return [self.player_1, self.player_2]

        if self.player_2.game_set == 3:
            print("Игрок 2 выиграл матч")
            return [self.player_1, self.player_2]

        if self.player_1.game == 6 and self.player_2.game == 6:
            return self.__tie_break_wrum_wrum()

        elif num == '1':
            game_score_up.player1_count_score()
            set_score_up.player1_set_win()
            return [self.player_1, self.player_2]

        elif num == '2':
            game_score_up.player2_count_score()
            set_score_up.player2_set_win()
            return [self.player_1, self.player_2]

    def __tie_break_wrum_wrum(self):
        tie_break_score = TieBreakScore(self.player_1, self.player_2)
        num = self.point_win_request

        set_score1 = self.player_1.game_set
        set_score2 = self.player_2.game_set

        if set_score1 + 1 == self.player_1.game_set:
            return [self.player_1, self.player_2]
        elif set_score2 + 1 == self.player_2.game_set:
            return [self.player_1, self.player_2]

        elif num == '1':
            tie_break_score.player1_tie_break_win()
            return [self.player_1, self.player_2]

        elif num == '2':
            tie_break_score.player2_tie_break_win()
            return [self.player_1, self.player_2]

