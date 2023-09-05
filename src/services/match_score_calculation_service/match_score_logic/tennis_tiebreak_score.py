class TieBreakScore:
    def __init__(self, player_score1_object, player_score2_object):
        self.player_score1_object = player_score1_object
        self.player_score2_object = player_score2_object

    def player1_tie_break_win(self):
        self.__tie_break_call(self.player_score1_object, self.player_score2_object)

    def player2_tie_break_win(self):
        self.__tie_break_call(self.player_score2_object, self.player_score1_object)

    def __tie_break_call(self, player_object_win, player_object_loose):
        """
        Вызов победы в тай-брейке
        :param player_object_win: игрок получивший очко
        :param player_object_loose: проигравший игрок
        """
        # Увеличиваем счетчик тай-брейка
        player_object_win.tie_break = player_object_win.tie_break + 1

        if player_object_win.tie_break == 7:
            if player_object_loose.tie_break <= 5:
                self.__change_score_with_tiebreak(player_object_win, player_object_loose)

        elif player_object_win.tie_break == 8:
            if player_object_loose.tie_break <= 6:
                self.__change_score_with_tiebreak(player_object_win, player_object_loose)

            # Действия при счете 8 = 8
            elif player_object_loose.tie_break == 8:
                player_object_win.tie_break = 7
                player_object_loose.tie_break = 7

        elif player_object_win.tie_break == 9:
            if player_object_loose.tie_break <= 7:
                self.__change_score_with_tiebreak(player_object_win, player_object_loose)

    @staticmethod
    def __change_score_with_tiebreak(player_object_win, player_object_loose):
        """
        Позволяет менять счет в сете при победе в тай-брейке
        :param player_object_win:
        :param player_object_loose:
        :return:
        """
        # Обнуляем тай-брейк
        player_object_win.tie_break = 0
        player_object_loose.tie_break = 0

        # Обнуляем Гейм
        player_object_win.game = 0
        player_object_loose.game = 0
        player_object_win.extra_move_score = 0
        player_object_loose.extra_move_score = 0

        player_object_win.game_set = player_object_win.game_set + 1
