import json
from src.services.finished_matches_persistence_service.interaction_table_matches.select_table_matches \
    import SelectTableMatches


class ObjectToJsonToDB:
    def __init__(self):
        """
        Класс нужен для сериализации объектов в JSON и
        наоборот, он помогает сохранять счет матча
        """
        pass

    @staticmethod
    def object_to_json(object_player_1, object_player_2):
        """
        Получаем JSON объект из наших данных для дальнейшей передачи в БД
        :return: json object
        """
        if object_player_1 is not None and object_player_2 is not None:
            data_players_score = {'player_1': object_player_1.__dict__,
                                  'player_2': object_player_2.__dict__}

            dict_to_json_players_score = json.dumps(data_players_score)
            return dict_to_json_players_score
        else:
            return 'no player objects, arguments init class == None'

    @staticmethod
    def db_str_to_dict(id_match):
        """
        Метод позволяет вытаскивать данные из БД
        :param id_match:
        :return:
        """
        # Извлекаем данные из таблицы
        start_class_match_object = SelectTableMatches()
        match_object = start_class_match_object.select_by_id(id_match)
        # Извлекаем информацию из столбца score
        score_data = match_object.Score
        # Загружаем информацию с помощью json
        data_to_json = json.loads(score_data)
        # Получаем данные счета игроков
        score_player1 = data_to_json['player_1']
        score_player2 = data_to_json['player_2']

        return [score_player1, score_player2]
