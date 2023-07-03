from src.serviсes.finished_matches_persistence_service.interaction_table_ABS \
    import InteractionTable
from src.data_base_directory.db_schema_conf import *


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