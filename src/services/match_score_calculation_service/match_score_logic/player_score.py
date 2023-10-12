class PlayerScore:
    def __init__(self, player_object_model, score_player=None):
        """

        :param player_object_model: Объект игрока из таблицы Player
        :param score_player: сериализованный Словарь из таблицы Match/Score
        """
        self.player_ID = player_object_model.ID
        self.player_name = player_object_model.Name
        # Параметры ниже получаются из
        # dict который можно получить из JSON
        if score_player is not None:
            self.score = score_player['score']
            self.game = score_player['game']
            self.game_set = score_player['game_set']
            self.tie_break = score_player['tie_break']
            # Дополнительное поле которое разыгрывается при ничьей
            self.extra_move_score = score_player['extra_move_score']
        elif score_player is None:
            self.score = 0
            self.game = 0
            self.game_set = 0
            self.tie_break = 0
            self.extra_move_score = 0

    def player_all_score_get(self):
        """
        Метод позволяет получить текущий счет.
        """
        __player_score = {
            "Счет": self.score,
            "Гейм": self.game,
            "Сет": self.game_set,
            "Тай-брейк": self.tie_break,
            "Extra-score": self.extra_move_score
        }

        print(f'{self.player_name}')
        print("----------")
        for key, value in __player_score.items():
            print(f"{key}: {value}")
        print("----------")
