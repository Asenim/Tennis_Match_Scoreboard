from src.finished_matches_persistence_service.interaction_table_ABS \
    import InteractionTable
from src.data_base_directory.db_schema_conf import *


class InteractionTableMatches(InteractionTable):
    def select_matches(self, name_p1=None, name_p2=None):
        """
        Метод в первую очередь будет выдавать всю
        информацию из таблицы Matches. Если получает
        на вход имена игроков ищет их сыгранные матчи
        и выводит на экран.
        :param name_p1: str: Имя игрока 1
        :param name_p2: str: Имя игрока 2
        :return:
        """
        session = Session(bind=engine)

        try:
            if name_p1 is not None and name_p2 is not None:
                player1_id = session.query(Players).filter(Players.Name == name_p1).one()
                player2_id = session.query(Players).filter(Players.Name == name_p2).one()

                select_match = session.query(Matches).filter(
                    Matches.Player1 == player1_id.ID,
                    Matches.Player2 == player2_id.ID
                )
                list_result = self.result_matches(select_match)
                self.output_console_list_result(list_result)

            else:
                select_all_matches = session.query(Matches).all()

                list_result = self.result_matches(select_all_matches)
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

    @staticmethod
    def result_matches(select_match):
        """
        Метод для формирования списка
        матчей после получения данных
        из Базы данных.
        :param select_match: выборка матчей,
            принимает объект session
        :return list_result: возвращает список
            с сыгранными матчами
        """
        list_result = []
        for select in select_match:
            list_add_in_list_result = [select.player1.Name,
                                       select.player2.Name,
                                       select.winner.Name]
            list_result.append(list_add_in_list_result)
        return list_result


matches = InteractionTableMatches()
matches.select_matches()
print('----')
matches.select_matches(name_p1='Sergey', name_p2='Alfob')
# matches.insert_matches(4, 5, 4)
# matches.insert_matches(5, 6, 5)
# matches.insert_matches(6, 4, 4)
# matches.insert_matches(4, 7, 4)
# matches.insert_matches(4, 8, 4)
# matches.insert_matches(4, 9, 4)
# matches.insert_matches(4, 10, 4)
