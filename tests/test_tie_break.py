import pytest
from tests.conftest import EmulationCycleMatch


class TestTieBreak:
    @pytest.mark.parametrize(
            'win_player_num, index_player_in_list, ex_tiebreak, ex_set',
            [('1', 0, 0, 1), ('2', 1, 0, 1)]
        )
    def test_tie_break_win_by_one_wicked(self, create_match_object, win_player_num, index_player_in_list, ex_tiebreak, ex_set):
        """
        Выигрыш тайбрейка в одну калитку.
        :param win_player_num: Игрок победивший в гейме
        :param index_player_in_list: индекс для получения объекта игрока
        :param ex_tiebreak: ожидаемый результат счета тайбрейка
        :param ex_set: ожидаемый результат счета сета
        """
        match = create_match_object

        # Доводим счет игроков до гейма = 5:5
        EmulationCycleMatch.emulation_match_win_cycle_game(20, match)
        # Доводим счет гейма до 6:6 для вызова тайбрейка
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score('1', 4, match)
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score('2', 4, match)

        # Далее доводим тай-бпейк одного из игроков до 6:0 (result тоже учавствует в этом процессе)
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score(win_player_num, 6, match)

        result = match.start_counting_score()

        # Проверяем результат
        assert result[index_player_in_list].tie_break == ex_tiebreak and result[index_player_in_list].game_set == ex_set

    @pytest.mark.parametrize(
            'win_player_num, index_player_in_list, ex_tiebreak, ex_set',
            [('1', 0, 0, 1), ('2', 1, 0, 1)]
        )
    def test_tie_break_win4_6(self,create_match_object, win_player_num, index_player_in_list, ex_tiebreak, ex_set):
        """
        Выигрыш сета при тайбрейке 4:6
        :param win_player_num: Игрок победивший в гейме
        :param index_player_in_list: индекс для получения объекта игрока
        :param ex_tiebreak: ожидаемый результат счета тайбрейка
        :param ex_set: ожидаемый результат счета сета
        """
        match = create_match_object

        # Доводим счет игроков до гейма = 5:5
        EmulationCycleMatch.emulation_match_win_cycle_game(20, match)
        # Доводим счет гейма до 6:6 для вызова тайбрейка
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score('1', 4, match)
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score('2', 4, match)

        # Далее доводим счет Тайбрейка обоих игроков до 4:4
        EmulationCycleMatch.emulation_match_win_cycle_score(4, match)

        # Далее доводим тай-бпейк одного из игроков до 6:4 (result тоже учавствует в этом процессе)
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score(win_player_num, 2, match)
        result = match.start_counting_score()

        # Проверяем результат
        assert result[index_player_in_list].tie_break == ex_tiebreak and result[index_player_in_list].game_set == ex_set

    @pytest.mark.parametrize(
            'win_player_num, index_player_in_list, ex_tiebreak, ex_set',
            [('1', 0, 0, 1), ('2', 1, 0, 1)]
        )
    def test_tie_break_win5_7(self, create_match_object, win_player_num, index_player_in_list, ex_tiebreak, ex_set):
        """
        Выигрыш сета при тайбрейке 5:7
        :param win_player_num: Игрок победивший в гейме
        :param index_player_in_list: индекс для получения объекта игрока
        :param ex_tiebreak: ожидаемый результат счета тайбрейка
        :param ex_set: ожидаемый результат счета сета
        """
        match = create_match_object

        # Доводим счет игроков до гейма = 5:5
        EmulationCycleMatch.emulation_match_win_cycle_game(20, match)
        # Доводим счет гейма до 6:6 для вызова тайбрейка
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score('1', 4, match)
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score('2', 4, match)

        # Далее доводим счет Тайбрейка обоих игроков до 5:5
        EmulationCycleMatch.emulation_match_win_cycle_score(5, match)

        # Далее доводим тай-бпейк одного из игроков до 7:5 (result тоже учавствует в этом процессе)
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score(win_player_num, 2, match)
        result = match.start_counting_score()

        # Проверяем результат
        assert result[index_player_in_list].tie_break == ex_tiebreak and result[index_player_in_list].game_set == ex_set

    @pytest.mark.parametrize(
            'win_player_num, index_player_in_list, ex_tiebreak, ex_set',
            [('1', 0, 0, 1), ('2', 1, 0, 1)]
        )
    def test_tie_break_win6_8(self, create_match_object, win_player_num, index_player_in_list, ex_tiebreak, ex_set):
        """
        Выигрыш сета при тайбрейке 6:8
        :param win_player_num: Игрок победивший в гейме
        :param index_player_in_list: индекс для получения объекта игрока
        :param ex_tiebreak: ожидаемый результат счета тайбрейка
        :param ex_set: ожидаемый результат счета сета
        """
        match = create_match_object

        # Доводим счет игроков до гейма = 6:6
        EmulationCycleMatch.emulation_match_win_cycle_game(20, match)
        # Доводим счет гейма до 6:6 для вызова тайбрейка
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score('1', 4, match)
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score('2', 4, match)

        # Далее доводим счет Тайбрейка обоих игроков до 6:6
        EmulationCycleMatch.emulation_match_win_cycle_score(6, match)

        # Далее доводим тай-бпейк одного из игроков до 8:6 (result тоже учавствует в этом процессе)
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score(win_player_num, 2, match)
        result = match.start_counting_score()

        # Проверяем результат
        assert result[index_player_in_list].tie_break == ex_tiebreak and result[index_player_in_list].game_set == ex_set

    @pytest.mark.parametrize(
            'win_player_num, index_player_in_list, ex_tiebreak, ex_set',
            [('1', 0, 8, 0), ('2', 1, 8, 0)]
        )
    def test_not_win_tiebreak(self,create_match_object, win_player_num, index_player_in_list, ex_tiebreak, ex_set):
        """
        Когда тайбрейк не заканчивается счет 6:6
        :param win_player_num: Игрок победивший в гейме
        :param index_player_in_list: индекс для получения объекта игрока
        :param ex_tiebreak: ожидаемый результат счета тайбрейка
        :param ex_set: ожидаемый результат счета сета
        """
        match = create_match_object

        # Доводим счет игроков до гейма = 5:5
        EmulationCycleMatch.emulation_match_win_cycle_game(20, match)
        # Доводим счет гейма до 6:6 для вызова тайбрейка
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score('1', 4, match)
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score('2', 4, match)

        # Далее доводим счет Тайбрейка обоих игроков до 7:7
        EmulationCycleMatch.emulation_match_win_cycle_score(7, match)
        match.point_win_request = win_player_num
        result = match.start_counting_score()

        # Проверяем результат
        assert result[index_player_in_list].tie_break == ex_tiebreak and result[index_player_in_list].game_set == ex_set

    @pytest.mark.parametrize(
            'win_player_num, index_player_in_list, ex_tiebreak, ex_set',
            [('1', 0, 8, 0), ('2', 1, 8, 0)]
        )
    def test_not_win_tiebreak2(self, create_match_object, win_player_num, index_player_in_list, ex_tiebreak, ex_set):
        """
        Когда тайбрейк не заканчивается счет 8:8
        А сбрасывается до 7:7
        :param win_player_num: Игрок победивший в гейме
        :param index_player_in_list: индекс для получения объекта игрока
        :param ex_tiebreak: ожидаемый результат счета тайбрейка
        :param ex_set: ожидаемый результат счета сета
        """
        match = create_match_object

        # Доводим счет игроков до гейма = 5:5
        EmulationCycleMatch.emulation_match_win_cycle_game(20, match)
        # Доводим счет гейма до 6:6 для вызова тайбрейка
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score('1', 4, match)
        EmulationCycleMatch.emulation_match_win_cycle_one_player_score('2', 4, match)

        # Далее доводим счет Тайбрейка обоих игроков до 8:8
        EmulationCycleMatch.emulation_match_win_cycle_score(8, match)

        match.point_win_request = win_player_num
        result = match.start_counting_score()

        # Проверяем результат
        assert result[index_player_in_list].tie_break == ex_tiebreak and result[index_player_in_list].game_set == ex_set
