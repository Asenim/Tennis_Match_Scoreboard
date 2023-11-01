from src.services.finished_matches_persistence_service.interaction_table_players.interaction_table_players \
    import InteractionTablePlayers
from src.services.finished_matches_persistence_service.interaction_table_matches.insert_table_matches \
    import InsertTableMatches
from src.services.match_score_calculation_service.match_score_logic.player_score import PlayerScore
from src.services.finished_matches_persistence_service.interaction_table_matches.object_to_json_to_db \
    import ObjectToJsonToDB


class NewMatchDataInsert:
    def __init__(self):
        self.interaction_table_players = InteractionTablePlayers()

    def treatment_new_match_data(self, request_body):
        list_for_treatment = self.__post_new_match_handler(request_body)
        player1_obj = list_for_treatment[0]
        player2_obj = list_for_treatment[1]
        id_matches = list_for_treatment[2]

        # Создаются объекты подсчета матча
        player1_obj_score = PlayerScore(player1_obj)
        player2_obj_score = PlayerScore(player2_obj)
        # Данные переводятся в формат json
        run_class_object_to_json = ObjectToJsonToDB()
        data_object_to_json = run_class_object_to_json.object_to_json(player1_obj_score, player2_obj_score)
        print(data_object_to_json)
        print(type(data_object_to_json))
        # Обновляются данные в БД
        update_matches_score = InsertTableMatches()
        update_matches_score.update_score_match(id_matches, data_object_to_json)

        return id_matches

    def __post_new_match_handler(self, request_body):
        """
        Обработка POST запроса из страницы нового матча.
        :param request_body: для парсинга данных из тела запроса.
        :return: Список со списком объектов игроков из БД и с ID матча
        """
        # Парсим полученную строку с именами
        str_request_body = str(request_body)
        # Убираем лишние символы из строки и разбиваем ее
        post_data = str_request_body.replace("'", "").split('&')
        # Отделяем игроков друг от друга для дальнейшей обработки
        post_data_player_1 = post_data[0]
        post_data_player_2 = post_data[1]
        # ong = OngoingMatchesService()
        print('post_data', post_data, 'player_1', post_data_player_1, 'player_2', post_data_player_2)
        # Вытаскиваем имена игроков
        # Разбиваем строку с именами игроков
        list_player_1 = post_data_player_1.split('=')
        list_player_2 = post_data_player_2.split('=')
        # Вытаскиваем из списков имена и убираем лишние пробелы
        player_1_name = list_player_1[1].replace(' ', '')
        player_2_name = list_player_2[1].replace(' ', '')
        # Добавляем игроков в Таблицу Players
        player_1_obj = self.interaction_table_players.insert_one_player_and_return_player_object(player_1_name)
        player_2_obj = self.interaction_table_players.insert_one_player_and_return_player_object(player_2_name)

        # Отправляем Игроков в таблицу Matches
        insert_players_in_match_table = InsertTableMatches()
        id_insert_match = insert_players_in_match_table.insert_matches(player_1_obj.ID, player_2_obj.ID)
        print('insert_data_obj', id_insert_match, dir(id_insert_match))

        return [
            player_1_obj,
            player_2_obj,
            id_insert_match
        ]
