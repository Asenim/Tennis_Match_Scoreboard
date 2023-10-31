import pytest
from tests.conftest import EmulationCycleMatch


class TestSet:
    @pytest.mark.parametrize(
        'win_player_num, index_player_in_list, ex_set',
        [('1', 0, 1), ('2', 1, 1)]
    )
    def test_players_win_set_by_one_wicked(self, create_match_object, win_player_num,
                                           index_player_in_list, ex_set):
        """
        Тестируем выигрыш сета в одну калитку
        :param win_player_num: Игрок победивший в гейме
        :param index_player_in_list: индекс для получения объекта игрока
        :param ex_set: ожидаемый результат счета сета
        """
        match = create_match_object

        for i in range(23):
            match.start_counting_score()

        result = match.start_counting_score()
        assert result[index_player_in_list].game_set == ex_set

    @pytest.mark.parametrize(
        'win_player_num, index_player_in_list, ex_set',
        [('1', 0, 1), ('2', 1, 1)]
    )
    def test_players_win_set(self, create_match_object, win_player_num,
                             index_player_in_list, ex_set):
        """
        Тестируем выигрыш сета при счете гейма = 5:6 + 1
        :param win_player_num: Игрок победивший в гейме
        :param index_player_in_list: индекс для получения объекта игрока
        :param ex_set: ожидаемый результат счета сета
        """
        match = create_match_object

        # Доводим счет игроков до гейма = 5:5
        EmulationCycleMatch.emulation_match_win_cycle_game(20, match)

        # Далее доаодим счет отдоного из игроков до 7:5 (result тоже учавствует в этом процессе)
        match.point_win_request = win_player_num
        for i in range(7):
            match.start_counting_score()
        result = match.start_counting_score()

        # Проверяем результат
        assert result[index_player_in_list].game_set == ex_set
