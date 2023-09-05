class PlayerScore:
    def __init__(self, player_name):
        self.__player_name = player_name
        self.score = 0
        self.game = 0
        self.game_set = 0
        self.tie_break = 0
        # Дополнительное поле которое разыгрывается при ничьей
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

        print(f'{self.__player_name}')
        print("----------")
        for key, value in __player_score.items():
            print(f"{key}: {value}")
        print("----------")
