import pytest
from tests.conftest import EmulationCycleMatch


class TestGame:
    @pytest.mark.parametrize(
        'win_player_num, index_player_in_list, ex_game, ex_score, ex_extra_move',
        [
            ('1', 0, 0, 40, 1), ('2', 1, 0, 40, 1)
        ]
    )
    def test_players_not_win_game(self, create_match_object, win_player_num,
                                  index_player_in_list, ex_game, ex_score, ex_extra_move):
        """
        Тест проверяет что гейм не закончится при счете 40:40 + 1 очко
        :param win_player_num: Игрок победивший в гейме
        :param index_player_in_list: индекс для получения объекта игрока
        :param ex_game: ожидаемый результат счета гейма
        :param ex_score: ожидаемый результат счета очков
        :param ex_extra_move: ожидаемый результат счета дополнительных очков
        """
        match = create_match_object
        # Цикл служит для того что бы довести счет игроков до 40:40
        EmulationCycleMatch.emulation_match_win_cycle_score(4, match)

        # Мы меняем счет игрока еще один раз что бы убедиться в том, что никто не выиграет гейм
        match.point_win_request = win_player_num
        result = match.start_counting_score()

        assert result[index_player_in_list].game == ex_game and\
               result[index_player_in_list].score == ex_score and\
               result[index_player_in_list].extra_move_score == ex_extra_move

    @pytest.mark.parametrize(
        'win_player_num, index_player_in_list, ex_game, ex_score, ex_extra_move',
        [('1', 0, 0, 40, 2), ('2', 1, 0, 40, 2)]
    )
    def test_players_not_win_game_2(self, create_match_object, win_player_num,
                                    index_player_in_list, ex_game, ex_score, ex_extra_move):
        """
        Тест проверяет что если два игрока набирают 2 дополнительных очка при счете 40:40
        эти доп очки сбрасываюся а гейм продолжается.
        :param win_player_num: Игрок победивший в гейме
        :param index_player_in_list: индекс для получения объекта игрока
        :param ex_game: ожидаемый результат счета гейма
        :param ex_score: ожидаемый результат счета очков
        :param ex_extra_move: ожидаемый результат счета дополнительных очков
        """
        match = create_match_object
        # Доводим score до 40:40
        EmulationCycleMatch.emulation_match_win_cycle_score(4, match)

        # Доводим extra move score до 2:2
        EmulationCycleMatch.emulation_match_win_cycle_score(2, match)

        # Проверяем что счетчик move score - сбросился
        result = match.start_counting_score()

        assert result[index_player_in_list].game == ex_game and \
               result[index_player_in_list].score == ex_score and \
               result[index_player_in_list].extra_move_score != ex_extra_move

    @pytest.mark.parametrize(
        'win_player_num, index_player_in_list, ex_game, ex_score',
        [('1', 0, 1, 0), ('2', 1, 1, 0)]
    )
    def test_players_win_game_by_one_wicked(self, create_match_object, win_player_num,
                                            index_player_in_list, ex_game, ex_score):
        """
        Тестируем выигрыш гейма в одну калитку
        :param win_player_num: Игрок победивший в гейме
        :param index_player_in_list: индекс для получения объекта игрока
        :param ex_game: ожидаемый результат счета гейма
        :param ex_score: ожидаемый результат счета очков
        """
        match = create_match_object
        for i in range(3):
            match.start_counting_score()

        result = match.start_counting_score()
        assert result[index_player_in_list].game == ex_game and \
               result[index_player_in_list].score == ex_score

    @pytest.mark.parametrize(
        'win_player_num, index_player_in_list, ex_game, ex_score',
        [('1', 0, 1, 0), ('2', 1, 1, 0)]
    )
    def test_players_win_game_by_30_40_score(self, create_match_object, win_player_num,
                                             index_player_in_list, ex_game, ex_score):
        """
        Тестируем выигрыш гейма при счете 30:40 + 1
        :param win_player_num: Игрок победивший в гейме
        :param index_player_in_list: индекс для получения объекта игрока
        :param ex_game: ожидаемый результат счета гейма
        :param ex_score: ожидаемый результат счета очков
        """
        match = create_match_object
        EmulationCycleMatch.emulation_match_win_cycle_score(3, match)

        match.point_win_request = win_player_num
        match.start_counting_score()
        result = match.start_counting_score()
        assert result[index_player_in_list].game == ex_game and result[index_player_in_list].score == ex_score

    @pytest.mark.parametrize(
        'win_player_num, index_player_in_list, ex_game, ex_score',
        [('1', 0, 1, 0), ('2', 1, 1, 0)]
    )
    def test_players_win_game_by_40_40_score(self, create_match_object, win_player_num,
                                             index_player_in_list, ex_game, ex_score):
        """
        Тестируем выигрыш гейма при счете 40:40 + 2
        :param win_player_num: Игрок победивший в гейме
        :param index_player_in_list: индекс для получения объекта игрока
        :param ex_game: ожидаемый результат счета гейма
        :param ex_score: ожидаемый результат счета очков
        """
        match = create_match_object
        EmulationCycleMatch.emulation_match_win_cycle_score(4, match)

        match.point_win_request = win_player_num
        match.start_counting_score()
        result = match.start_counting_score()
        assert result[index_player_in_list].game == ex_game and result[index_player_in_list].score == ex_score
