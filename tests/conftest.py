import pytest
from src.services.match_score_calculation_service.match_start import MatchStart
from tests.tests_data import *


@pytest.fixture()
def create_match_object(win_player_num):
    match = MatchStart(id_match=1, player1_object_model=player_1,
                       player2_object_model=player_2,
                       player1_score=score_player_1,
                       player2_score=score_player_2, point_win_request=win_player_num)

    return match


class EmulationCycleMatch:
    @staticmethod
    def emulation_match_win_cycle_one_player_score(num_win_player, cycle_range_num, object_match):
        """
        Цикл служит для того что бы довести счет игроков до нужных нам значений
        и дальнейшей проверки.
        Работает с любым количеством итераций.
        :param num_win_player: Номер победившего игрока (Строка)
        :param cycle_range_num: Количество итераций для нужного результата.
        :param object_match: Объект матча.
        :return:
        """
        object_match.point_win_request = num_win_player
        for i in range(cycle_range_num):
            object_match.start_counting_score()

    @staticmethod
    def emulation_match_win_cycle_score(cycle_range_num, object_match):
        """
        Цикл служит для того что бы довести счет игроков до нужных нам значений
        и дальнейшей проверки.
        P.S. Не работает более чем на 4 итерации.
        :param cycle_range_num: Количество итераций для нужного результата.
        :param object_match: Объект матча.
        """
        for i in range(cycle_range_num):
            object_match.point_win_request = '1'
            object_match.start_counting_score()

            object_match.point_win_request = '2'
            object_match.start_counting_score()

    @staticmethod
    def emulation_match_win_cycle_game(cycle_range_num, object_match):
        """
        Цикл служит для того что бы довести Гейм игроков до нужных нам значений
        и дальнейшей проверки.
        P.S. Работает корректно до 22 итераций (не может сделать гейм = 6:6)
        :param cycle_range_num: Количество итераций для нужного результата.
        :param object_match: Объект матча.
        """

        for i in range(cycle_range_num):
            object_match.point_win_request = '1'
            object_match.start_counting_score()

        for i in range(cycle_range_num):
            object_match.point_win_request = '2'
            object_match.start_counting_score()
