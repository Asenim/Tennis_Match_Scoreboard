from src.data_base_directory.db_schema_conf import *
import logging


# players
class InteractionTablePlayers:
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
                session.delete(__player)
                session.commit()
                print(f"Data {__player} deleted!")
            else:
                __player = session.query(Players).filter(Players.Name == name).one()
                session.delete(__player)
                session.commit()
                print(f"Data {__player} deleted!")

        except ConnectionError:
            print("Failed to connect to database")
        finally:
            session.close()
            print("Session closed!")


class InteractionTableMatches:
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
            session.add(__insert_match)
            print(session.new)
            session.commit()
            print("Data added to db")
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
            session.delete(__player)
            session.commit()
            print(f"Data {__player} deleted!")

        except ConnectionError:
            print("Failed to connect to database")
        finally:
            session.close()
            print("Session closed!")


play = InteractionTablePlayers()
# play.insert_one_player('Alfob')
# play.insert_one_player('Ziya')
# play.insert_one_player('Kubla')
# play.insert_one_player('Sergey')
# play.delete_one_player(id=3)
# play.delete_one_player(name='Ziya')

matches = InteractionTableMatches()
# matches.insert_matches(3, 4, 4)
