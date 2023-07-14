from .interaction_table_matches_ABS import InteractionTableMatchesABS
from src.data_base_directory.db_schema_conf import *


class DeleteTableMatches(InteractionTableMatchesABS):
    @staticmethod
    def delete_matches(id_match):
        """
        Функция удаляет данные из таблицы matches
        по ID.
        :param id_match: ID матча который будем удалять
        """
        session = Session(bind=engine)
        try:
            __player = session.query(Player).filter(Matche.ID == id_match).one()

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
