class TennisGameScore:
    def __init__(self, player_score1_object, player_score2_object):
        """
        Класс позволяет вести счет и
        подсчитывать геймы.
        :param player_score1_object: Принимает на вход объект счета игрока.
        :param player_score2_object: Принимает на вход объект счета игрока.
        """
        self.__player1_score = player_score1_object
        self.__player2_score = player_score2_object

    def player1_count_score(self):
        """
        Позволяет первому игроку получить очко.
        :return:
        """
        self.__player_count_score(self.__player1_score, self.__player2_score)

    def player2_count_score(self):
        """
        Позволяет второму игроку получить очко.
        :return:
        """
        self.__player_count_score(self.__player2_score, self.__player1_score)

    def __player_count_score(self, player_score_win, player_score_loose):
        """
        Метод позволяет увеличить очки и определить победителя в гейме.
        :param player_score_win: передается объект класса игрок, который побеждает
        :param player_score_loose: передается объект класса игрок, который проигрывает
        :return:
        """
        if player_score_win.score == 0 or player_score_win.score == 15:
            player_score_win.score = player_score_win.score + 15

        elif player_score_win.score == 30:
            player_score_win.score = player_score_win.score + 10

            if player_score_loose.score <= 15:
                self.__winner_score()

        elif player_score_win.score == 40:
            player_score_win.extra_move_score = player_score_win.extra_move_score + 1

            if player_score_win.extra_move_score - 1 > player_score_loose.extra_move_score:
                self.__winner_score()

            if player_score_loose.score <= 30 and player_score_win.extra_move_score == 1:
                self.__winner_score()

            self.__score_breaker()

    def __score_breaker(self):
        """
        Границы счетчика доп. очков
        :return:
        """
        if self.__player1_score.extra_move_score == self.__player2_score.extra_move_score:
            self.__player1_score.extra_move_score = 0
            self.__player2_score.extra_move_score = 0

        if self.__player1_score.extra_move_score > 2:
            self.__player1_score.extra_move_score = 2

        if self.__player2_score.extra_move_score > 2:
            self.__player2_score.extra_move_score = 2

    def __winner_score(self):
        """
        Метод позволяет определить победителя по
        результатам очков.
        :return:
        """
        if self.__player1_score.score == 40 and self.__player1_score.extra_move_score > 0:
            print()
            self.__player1_score.game = self.__player1_score.game + 1
            print()
            print('Cчет: ')
            self.__player1_score.player_all_score_get()

            self.__player1_score.score = 0
            self.__player2_score.score = 0
            self.__player1_score.extra_move_score = 0
            self.__player2_score.extra_move_score = 0
            print()

        elif self.__player2_score.score == 40 and self.__player2_score.extra_move_score > 0:
            print()
            self.__player2_score.game = self.__player2_score.game + 1
            print()
            print('Cчет: ')
            self.__player2_score.player_all_score_get()
            self.__player1_score.score = 0
            self.__player2_score.score = 0
            self.__player1_score.extra_move_score = 0
            self.__player2_score.extra_move_score = 0
            print()
