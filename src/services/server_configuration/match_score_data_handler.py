from src.services.finished_matches_persistence_service.interaction_table_matches.select_table_matches \
    import SelectTableMatches
from src.services.finished_matches_persistence_service.interaction_table_players.select_table_players \
    import SelectInteractionTablePlayers
from src.services.finished_matches_persistence_service.interaction_table_matches.object_to_json_to_db \
    import ObjectToJsonToDB
from src.services.match_score_calculation_service.match_start import MatchStart


class MatchScoreDataHandler:
    def __init__(self):
        self.run_class_select_table_matches = SelectTableMatches()
        self.run_class_select_players = SelectInteractionTablePlayers()
        self.run_class_object_to_json = ObjectToJsonToDB()

    def treatment_match_score_data(self, post_request_data):
        # Получаем id текущего матча
        key_value_id_match = post_request_data[0].split('=')
        id_current_match = key_value_id_match[1]
        # Получаем номер победившего игрока
        key_value_player = post_request_data[1].split('=')
        num_win_player = key_value_player[1]

        # Достаем ID игроков из таблицы матча
        record_table_matches = self.run_class_select_table_matches.select_by_id(id_current_match)
        id_player_1 = record_table_matches.Player1
        id_player_2 = record_table_matches.Player2
        print('id_players', id_player_1, id_player_2)
        # Достаем самих игроков из таблицы игроков

        player_1_object = self.run_class_select_players.select_one_player(player_id=id_player_1)
        player_2_object = self.run_class_select_players.select_one_player(player_id=id_player_2)
        print('player_object', player_1_object.Name, player_2_object.Name)
        # Получаем текущий счет

        current_score = self.run_class_object_to_json.db_str_to_dict(id_current_match)
        player_1_score = current_score[0]
        player_2_score = current_score[1]
        print(player_1_score, player_2_score)

        # Запускаем логику приложения, меняем счет игроков и возвращаем объекты игроков
        run_class_match_start = MatchStart(id_match=id_current_match,
                                           player1_object_model=player_1_object,
                                           player2_object_model=player_2_object,
                                           player1_score=player_1_score,
                                           player2_score=player_2_score,
                                           point_win_request=num_win_player)

        start_count_score = run_class_match_start.start_counting_score()
        score_player_1_object = start_count_score[0]
        score_player_2_object = start_count_score[1]

        return [score_player_1_object, score_player_2_object, id_current_match]
