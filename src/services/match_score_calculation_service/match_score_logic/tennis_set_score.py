"""
Одно очко начисляется каждые 6
геймов (game_of_tennis) победившему
игроку

Матч играется до 3x сетов
(Подумать над реализацией
5ти сетового матча)
"""


class TennisSetScore:
    def __init__(self, player_score1_object, player_score2_object):
        """
        Класс позволяет вести счет и
        подсчитывать сеты.
        :param player_score1_object: Принимает на вход объект счета игрока.
        :param player_score2_object: Принимает на вход объект счета игрока.
        """
        self.__player1_score = player_score1_object
        self.__player2_score = player_score2_object

    def player1_set_win(self):
        self.__player_set_win(self.__player1_score, self.__player2_score)

    def player2_set_win(self):
        self.__player_set_win(self.__player2_score, self.__player1_score)

    def __player_set_win(self, player_object_win, player_object_loose):
        """
        Данный метод позволяет нам увеличивать очки
        при победе в сете.
        :param player_object_win: передается объект класса игрок, который побеждает в сете.
        :param player_object_loose: передается объект класса игрок, который проигрывает в сете.
        :return:
        """
        if player_object_win.game == 6:
            if player_object_loose.game <= 4:
                self.__change_set_score(player_object_win, player_object_loose)

        elif player_object_win.game == 7:
            if player_object_loose.game <= 5:
                self.__change_set_score(player_object_win, player_object_loose)

    @staticmethod
    def __change_set_score(player_object_win, player_object_loose):
        """
        Позволяет менять счетчики при победе в сете
        :param player_object_win:
        :param player_object_loose:
        :return:
        """
        player_object_win.game_set = player_object_win.game_set + 1

        player_object_win.game = 0
        player_object_loose.game = 0
        player_object_win.extra_move_score = 0
        player_object_loose.extra_move_score = 0
