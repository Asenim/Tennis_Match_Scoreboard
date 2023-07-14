from src.serviсes.finished_matches_persistence_service.interaction_table_ABS \
    import InteractionTableABS
from src.data_base_directory.db_schema_conf import *


class InteractionTablePlayers(InteractionTableABS):
    @staticmethod
    def insert_one_player(name):
        """
        Функция добавляет игроков в таблицу players
        :return:
        """
        session = Session(bind=engine)
        try:
            __player = Player(
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
    def delete_one_player(name=None, uniq_id=None):
        """
        Функция будет удалять игроков из таблицы players
        :return:
        """
        session = Session(bind=engine)
        try:
            if uniq_id is not None:
                __player = session.query(Player).filter(Player.ID == uniq_id).one()

                session.delete(__player)
                session.commit()
                print(f"Data {__player.ID, __player.Name} deleted!")

            else:
                __player = session.query(Player).filter(Player.Name == name).one()

                session.delete(__player)
                session.commit()
                print(f"Data {__player.ID, __player.Name} deleted!")

        except ConnectionError:
            print("Failed to connect to database")
        finally:
            session.close()
            print("Session closed!")


if "__main__" == __name__:
    play = InteractionTablePlayers()
    # print(play.select_one_player('Kiril'))
    # print(play.select_one_player('Seva'))
    play.insert_one_player('Alfob')
    # play.insert_one_player('Alsu')
    # play.insert_one_player('Pasha')
    # play.insert_one_player('Misha')
    # play.insert_one_player('Asta')
    # play.insert_one_player('Lina')
    # play.insert_one_player('Ichigo')
    # play.insert_one_player('Sergey')
    # play.delete_one_player(uniq_id=13)
    # play.delete_one_player(name='Ziya')
    # play.insert_one_player("Ziya")
    # play.delete_one_player(name="Ziya")
