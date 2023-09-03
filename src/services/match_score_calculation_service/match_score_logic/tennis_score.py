"""
Счет по правилам тенниса
По результатам счета определяется
очко в Гейме (game_of_tennis)

### Тест кейсы ###
1. Проверка победы первого игрока при:

"""


class TennisScore:
    def __init__(self, player_score1_object, player_score2_object):
        self.__player1_score = player_score1_object
        self.__player2_score = player_score2_object

    def player1_count_score(self):
        """
        Позволяет первому игроку получить очко.
        :return:
        """
        if self.__player1_score.score == 0 or self.__player1_score.score == 15:
            self.__player1_score.score = self.__player1_score.score + 15

        elif self.__player1_score.score == 30:
            self.__player1_score.score = self.__player1_score.score + 10

            if self.__player2_score.score <= 15:
                self.__winner_score()

        elif self.__player1_score.score == 40:
            self.__player1_score.draw = self.__player1_score.draw + 1

            if self.__player1_score.draw - 1 > self.__player2_score.draw:
                self.__winner_score()

            if self.__player2_score.score == 30 and self.__player1_score.draw == 1:
                self.__winner_score()

            self.__score_breaker()

    def player2_count_score(self):
        """
        Позволяет второму игроку получить очко.
        :return:
        """
        if self.__player2_score.score == 0 or self.__player2_score.score == 15:
            self.__player2_score.score = self.__player2_score.score + 15

        elif self.__player2_score.score == 30:
            self.__player2_score.score = self.__player2_score.score + 10

            if self.__player1_score.score <= 15:
                self.__winner_score()

        elif self.__player2_score.score == 40:
            self.__player2_score.draw = self.__player2_score.draw + 1

            if self.__player1_score.draw < self.__player2_score.draw - 1:
                self.__winner_score()

            if self.__player1_score.score == 30 and self.__player2_score.draw == 1:
                self.__winner_score()

            self.__score_breaker()

    def __score_breaker(self):
        """
        Позволяет определить победителя в счете.
        :return:
        """
        if self.__player1_score.draw == self.__player2_score.draw:
            self.__player1_score.draw = 0
            self.__player2_score.draw = 0

        if self.__player1_score.draw > 2:
            self.__player1_score.draw = 2

        if self.__player2_score.draw > 2:
            self.__player2_score.draw = 2

    def __winner_score(self):
        """
        Метод позволяет определить победителя по
        результатам очков.
        :return:
        """
        if self.__player1_score.score == 40 and self.__player1_score.draw > 0:
            print()
            print('Игрок 1 победил')
            print('----------------')
            print('Cчет: ')
            print(self.current_account())
            self.__player1_score.score = 0
            self.__player2_score.score = 0
            self.__player1_score.draw = 0
            self.__player2_score.draw = 0
            print()

        elif self.__player2_score.score == 40 and self.__player2_score.draw > 0:
            print()
            print('Игрок 2 победил')
            print('----------------')
            print('Cчет: ')
            print(self.current_account())
            self.__player1_score.score = 0
            self.__player2_score.score = 0
            self.__player1_score.draw = 0
            self.__player2_score.draw = 0
            print()

    def current_account(self):
        """
        Метод позволяет получить текущий счет.
        :return __players_score: кортеж с текущим счетом
        """
        __players_score = ([self.__player1_score.score, self.__player1_score.draw],
                           [self.__player2_score.score, self.__player2_score.draw])
        return __players_score
