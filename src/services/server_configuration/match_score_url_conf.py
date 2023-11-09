from src.services.finished_matches_persistence_service.interaction_table_matches.object_to_json_to_db \
    import ObjectToJsonToDB
from src.services.finished_matches_persistence_service.interaction_table_matches.select_table_matches \
    import SelectTableMatches
from src.services.finished_matches_persistence_service.interaction_table_players.select_table_players \
    import SelectInteractionTablePlayers
from src.services.match_score_calculation_service.match_score_logic.player_score import PlayerScore
from src.samples.match_calculation_samples import jinja2_result_page_calculation


class MatchScoreUrlConf:
    def __init__(self, ip_addr):
        """
        Класс для получения и формирование всех данных, для дальнейшего
        формирования страницы и отдачи ее пользователю
        """
        self.start_class_select_matches = SelectTableMatches()
        self.start_class_select_players = SelectInteractionTablePlayers()
        self.run_class_object_to_json = ObjectToJsonToDB()
        self.ip_address = ip_addr

    def page_formation_for_match_score(self, id_matches):
        """
        Формируем страницу для подсчета матча
        :param id_matches:
        :return result_page: страница для отрисовки
        """
        # Получаем объекты игроков текущего матча
        match_record = self.start_class_select_matches.select_by_id(id_matches)
        player_1_id = match_record.Player1
        player_2_id = match_record.Player2
        player_1_object = self.start_class_select_players.select_one_player(player_id=player_1_id)
        player_2_object = self.start_class_select_players.select_one_player(player_id=player_2_id)
        # Получаем данные счета из json
        get_data_in_python_is_json = self.run_class_object_to_json.db_str_to_dict(id_matches)
        score_player_1 = get_data_in_python_is_json[0]
        score_player_2 = get_data_in_python_is_json[1]
        # Создаём объекты для отрисовки
        player1_obj_score = PlayerScore(player_1_object, score_player=score_player_1)
        player2_obj_score = PlayerScore(player_2_object, score_player=score_player_2)

        result_page = jinja2_result_page_calculation.generate_result_page_calculation(
            player1_obj_score, player2_obj_score, id_matches, self.ip_address
        )

        return result_page
