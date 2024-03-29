from src.services.finished_matches_persistence_service.interaction_table_ABS import InteractionTableABS
from src.data_base_directory.db_schema_conf import *


class SelectInteractionTablePlayers(InteractionTableABS):
    def select_all(self):
        """
        Метод выбирает всех игроков из таблицы
        Players и возвращает эту информацию в
        виде списка.
        :return list_result: список записей
            всех сыгранных матчей
        """
        session = Session(bind=engine)

        try:
            select_all_players = session.query(Player).all()
            list_result = self.__result_players(select_all_players)
            self.output_console_list_result(list_result)

            return list_result

        except ConnectionError:
            print("Connecting Error")

        finally:
            session.close()
            print("Session closed!")

    @staticmethod
    def select_one_player(player_name=None, player_id=None):
        """
        Метод служит для выбора одного игрока из таблицы
        Players по имени и возвращает ОБЪЕКТ записи игрока.
        :return: Объект записи из таблицы players
        """
        session = Session(bind=engine)

        try:
            if player_name is not None:
                # Получаем объект игрока из базы данных.
                player_object = session.query(Player).filter(Player.Name == player_name).first()
                return player_object
            elif player_id is not None:
                player_object = session.query(Player).filter(Player.ID == player_id).first()
                return player_object

        except ConnectionError:
            print("Connecting Error")

        finally:
            session.close()
            print("Session closed!")

    @staticmethod
    def __result_players(select_player):
        """
        Метод для формирования списка
        игроков после получения данных
        из Базы данных.
        :param select_player: выборка игроков,
            принимает объект session
        :return list_result: возвращает список
            с сыгранными матчами
        """
        list_result = []
        for select in select_player:
            list_add_in_list_result = [select.ID,
                                       select.Name]
            list_result.append(list_add_in_list_result)
        return list_result
