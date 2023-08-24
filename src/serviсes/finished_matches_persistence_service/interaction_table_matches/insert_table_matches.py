from .interaction_table_matches_ABS import InteractionTableMatchesABS
from src.data_base_directory.db_schema_conf import *


class InsertTableMatches(InteractionTableMatchesABS):
    @staticmethod
    def insert_matches(p1_id, p2_id, p_win):
        """
        Функция добавляет результаты игры в таблицу matches
        В эту таблицу могут быть добавлены только игроки из
        таблицы Player.
        :param p1_id: ID player1 (Column name: Player1)
        :param p2_id: ID player2 (Column name: Player2)
        :param p_win: ID player winner (Column name: Winner)
        """
        session = Session(bind=engine)
        try:
            __insert_match = Match(
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
