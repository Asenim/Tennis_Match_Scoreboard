from .interaction_table_matches_ABS import InteractionTableMatchesABS
from src.data_base_directory.db_schema_conf import *


class InsertTableMatches(InteractionTableMatchesABS):
    @staticmethod
    def insert_matches(p1_id, p2_id, p_win=None):
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

                session.flush()
                match_id = __insert_match.ID
                return match_id

            except ValueError:
                print("There are no players with this ID in the players table")

        except ConnectionError:
            print("Failed to connect to database")
        finally:
            session.commit()
            print("Data added to db")
            session.close()
            print("Session closed!")

    def insert_winner_player_id(self):
        pass

    @staticmethod
    def update_score_match(id_match, json_object):
        """
        Функция служит для обновления счета матча
        во время работы программы
        1. Мы очищаем поле score
        2. Добавляем туда информацию о счете матча.
        :param id_match: нужен для получения экземпляра матча из БД
        :param json_object: нужен для замены информации в колонке score
        :return:
        """
        session = Session(bind=engine)
        try:
            update_object_match = session.query(Match).filter(id_match == Match.ID).first()

            try:
                update_object_match.Score = None
                session.flush()
                # session.commit()
                update_object_match.Score = json_object
                #session.add(update_object_match)
                session.commit()
                print("Data added to db")

            except ValueError:
                print("There are no players with this ID in the players table")

        except ConnectionError:
            print("Failed to connect to database")
        finally:
            # session.commit()
            # print("Data added to db")
            session.close()
            print("Session closed!")
