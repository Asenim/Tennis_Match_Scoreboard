import pytest
from tests.conftest import EmulationCycleMatch


class TestMatch:
    @pytest.mark.parametrize(
        "win_player_num, index_player_in_list, expected_result",
        [('1', 0, 3), ('2', 1, 3)]
    )
    def test_players_win_match(self, create_match_object, win_player_num, index_player_in_list, expected_result):
        """
        :param win_player_num: Игрок победивший в гейме
        :param index_player_in_list: индекс для получения объекта игрока
        :param expected_result: Ожидаемый результат матча
        """
        match = create_match_object

        EmulationCycleMatch.emulation_match_win_cycle_one_player_score(win_player_num, 72, match)
        # Метод срабатывает 73 раз и помогает нам убедиться что результат не изменится
        result = create_match_object.start_counting_score()
        assert result[index_player_in_list].game_set == expected_result
