"""
Счет по правилам тенниса
По результатам счета определяется
очко в Гейме (game_of_tennis)
"""


class TennisScore:
    def __init__(self, player_score1_object, player_score2_object):
        self.__player1_score = player_score1_object
        self.__player2_score = player_score2_object

    def player1_win_score(self):
        """
        Позволяет первому игроку получить очко.
        :return:
        """
        if self.__player1_score == 0 or self.__player1_score == 15:
            self.__player1_score = self.__player1_score + 15

        elif self.__player1_score == 30:
            self.__player1_score = self.__player1_score + 10

    def player2_win_score(self):
        """
        Позволяет второму игроку получить очко.
        :return:
        """
        if self.__player2_score == 0 or self.__player2_score == 15:
            self.__player2_score = self.__player2_score + 15

        elif self.__player2_score == 30:
            self.__player2_score = self.__player2_score + 10

    def __score_winner(self):
        """
        Позволяет определить победителя в счете.
        :return:
        """
        pass

    def current_account(self):
        """
        Метод позволяет получить текущий счет.
        :return __players_score: кортеж с текущим счетом
        """
        __players_score = (self.__player1_score, self.__player2_score)
        return __players_score

#
# if "__main__" == __name__:
#     ts = TennisScore()
#     while True:
#         control = input("Введите 1, 2 или s ")
#
#         if control == '1':
#             ts.player1_win_score()
#             print(ts.current_account())
#
#         elif control == '2':
#             ts.player2_win_score()
#             print(ts.current_account())
#
#         elif control == 's':
#             break
