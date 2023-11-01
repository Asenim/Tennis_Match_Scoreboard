from src.services.finished_matches_persistence_service.interaction_table_ABS \
    import InteractionTableABS
from src.data_base_directory.db_schema_conf import *


class InteractionTablePlayers(InteractionTableABS):
    @staticmethod
    def insert_one_player_and_return_player_object(name):
        """
        Функция добавляет игроков в таблицу players
        :return:
        """
        session = Session(bind=engine)
        try:
            player_object = session.query(Player).filter_by(Name=name).first()
            # Проверяем существование игрока в Таблице
            if player_object:
                print('Существующий объект игрока', player_object)
                return player_object
            else:
                __player = Player(
                    Name=name
                )

                session.add(__player)
                session.commit()
                print("Data added to db")
                added_player_object = session.query(Player).filter_by(Name=name).first()
                return added_player_object

        except ConnectionError:
            print("Failed to connect to database")

        finally:
            session.close()
            print("Session closed!")

    @staticmethod
    def delete_one_player(name=None, uniq_id=None):
        """
        Функция будет удалять игроков из таблицы players
        Функция не используется в проекте.
        :return:
        """
        session = Session(bind=engine)
        try:
            if uniq_id is not None:
                __player = session.query(Player).filter_by(Player.ID == uniq_id).one()
                if __player:
                    session.delete(__player)
                    session.commit()
                    print(f"Data {__player.ID, __player.Name} deleted!")
                else:
                    print('Object is none in db')

            else:
                __player = session.query(Player).filter_by(Player.Name == name).one()
                if __player:
                    session.delete(__player)
                    session.commit()
                    print(f"Data {__player.ID, __player.Name} deleted!")
                else:
                    print('Object is none in db')

        except ConnectionError:
            print("Failed to connect to database")
        finally:
            session.close()
            print("Session closed!")
