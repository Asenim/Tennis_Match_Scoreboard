from src.data_base_directory.db_schema_conf import *
# import json
# import logging


class InteractionTable:
    @staticmethod
    def output_console_list_result(list_output):
        """
        Метод позволяет выводить в консоль информацию
        о всех выборках.
        :param list_output: параметр принимает в себя
        список с результатами выборки.
        """
        for item in list_output:
            print(*item)


# players
class InteractionTablePlayers(InteractionTable):
    @staticmethod
    def insert_one_player(name):
        """
        Функция добавляет игроков в таблицу players
        :return:
        """
        session = Session(bind=engine)
        try:
            __player = Players(
                Name=name
            )
            session.add(__player)
            print(session.new)
            session.commit()
            print("Data added to db")
        except ConnectionError:
            print("Failed to connect to database")
        finally:
            session.close()
            print("Session closed!")

    @staticmethod
    def delete_one_player(name=None, id=None):
        """
        Функция будет удалять игроков из таблицы players
        :return:
        """
        session = Session(bind=engine)
        try:
            if id is not None:
                __player = session.query(Players).filter(Players.ID == id).one()

                try:
                    session.delete(__player)
                    session.commit()
                    print(f"Data {__player} deleted!")
                except ValueError:
                    print('There are no players with this ID in the players table')
            else:
                __player = session.query(Players).filter(Players.Name == name).one()

                try:
                    session.delete(__player)
                    session.commit()
                    print(f"Data {__player} deleted!")
                except ValueError:
                    print('There are no players with this Name in the players table')

        except ConnectionError:
            print("Failed to connect to database")
        finally:
            session.close()
            print("Session closed!")


class InteractionTableMatches(InteractionTable):
    def select_matches(self, id_p1=None, id_p2=None,
                       name_p1=None, name_p2=None):
        """
        Метод в первую очередь будет выдавать всю
        информацию из таблицы Matches
        :param id_p1:
        :param id_p2:
        :param name_p1:
        :param name_p2:
        :return:
        """
        session = Session(bind=engine)

        try:
            select_all_matches = session.query(Matches).all()

            list_result = []
            for select in select_all_matches:
                list_add_in_list_result = [select.players1.Name,
                                           select.players2.Name,
                                           select.winners.Name]
                list_result.append(list_add_in_list_result)

            self.output_console_list_result(list_result)

        except ConnectionError:
            print("Connecting Error")
        finally:
            session.close()
            print("Session closed!")

    @staticmethod
    def insert_matches(p1_id, p2_id, p_win):
        """
        Функция добавляет результаты игры в таблицу matches
        В эту таблицу могут быть добавлены только игроки из
        таблицы Players.
        :param p1_id: ID player1 (Column name: Player1)
        :param p2_id: ID player2 (Column name: Player2)
        :param p_win: ID player winner (Column name: Winner)
        """
        session = Session(bind=engine)
        try:
            __insert_match = Matches(
                Player1=p1_id,
                Player2=p2_id,
                Winner=p_win,
            )

            try:
                session.add(__insert_match)
                print(session.new)
                session.commit()
                print("Data added to db")
            except ValueError:
                print("There are no players with this ID in the players table")

        except ConnectionError:
            print("Failed to connect to database")
        finally:
            session.close()
            print("Session closed!")

    @staticmethod
    def delete_matches(id_match):
        """
        Функция удаляет данные из таблицы matches
        по ID.
        :param id_match: ID матча который будем удалять
        """
        session = Session(bind=engine)
        try:
            __player = session.query(Players).filter(Matches.ID == id_match).one()

            try:
                session.delete(__player)
                session.commit()
                print(f"Data {__player} deleted!")
            except ValueError:
                print("there are no matches with this ID in the matches table")

        except ConnectionError:
            print("Failed to connect to database")
        finally:
            session.close()
            print("Session closed!")


play = InteractionTablePlayers()
# play.insert_one_player('Alfob')
# play.insert_one_player('Alsu')
# play.insert_one_player('Pasha')
# play.insert_one_player('Misha')
# play.insert_one_player('Asta')
# play.insert_one_player('Lina')
# play.insert_one_player('Ichigo')
# play.insert_one_player('Sergey')
# play.delete_one_player(id=3)
# play.delete_one_player(name='Ziya')

matches = InteractionTableMatches()
matches.select_matches()
# matches.insert_matches(4, 5, 4)
# matches.insert_matches(5, 6, 5)
# matches.insert_matches(6, 4, 4)
# matches.insert_matches(4, 7, 4)
# matches.insert_matches(4, 8, 4)
# matches.insert_matches(4, 9, 4)
# matches.insert_matches(4, 10, 4)
