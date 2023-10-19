from src.services.finished_matches_persistence_service.interaction_table_matches.interaction_table_matches_ABS \
    import InteractionTableMatchesABS
from src.data_base_directory.db_schema_conf import *
from sqlalchemy import func


class SelectTableMatches(InteractionTableMatchesABS):
    # @staticmethod
    def select_all(self, param_offset, param_limit):
        """
        Метод выбирает все матчи из таблицы
        Matches и возвращает эту информацию в
        виде списка.
        :param param_offset: Параметр для определения смещения страницы.
        :param param_limit: Параметр для обозначения лимита записей на странице.
        :return select_all_matches: список записей
            всех сыгранных матчей
        """
        session = Session(bind=engine)

        try:
            select_all_matches = session.query(Match).filter(Match.Winner != None)\
                .offset(param_offset).limit(param_limit).all()
            list_result = self.result_matches(select_all_matches)
            count_all_matches = session.query(Match).filter(Match.Winner != None).count()

            return [list_result, count_all_matches]

        except ConnectionError:
            print("Connecting Error")

        finally:
            session.close()
            print("Session closed!")

    def selection_by_two_names(self, name_p1, name_p2):
        """
        Метод делает выборку из талицы по столбцам
        name_p1 = Player1, name_p2 = Player2.
        Если в нашей таблице Matches есть запись с именами
        name_p1 и name_p2 - то метод отобразит этот матч
        :param name_p1: Имя первого игрока для поиска в столбце
            Player1
        :param name_p2: Имя второго игрока для поиска в столбце
            Player2
        :return list_result: список с записями где есть игроки
            с обоими именами.
        """
        session = Session(bind=engine)

        try:
            # Получаем два объекта игрока.
            player_object_1 = session.query(Player).filter(Player.Name == name_p1).one()
            player_object_2 = session.query(Player).filter(Player.Name == name_p2).one()

            # Делаем выборку фильтруя по обоим столбцам и игрокам
            select_match = session.query(Match).filter(
                Match.Player1 == player_object_1.ID,
                Match.Player2 == player_object_2.ID,
                Match.Winner != None
            )

            list_result = self.result_matches(select_match)
            return list_result

        except ConnectionError:
            print("Connecting Error")

        finally:
            session.close()
            print("Session closed!")

    def selection_by_one_name(self, player_name, param_offset, param_limit):
        """
        Метод делает выборку из талицы по столбцу
        name_p1 = Player1 и name_p1 = Player2
        Если в нашей таблице Match есть записи с именем
        name_p1 - то метод отобразит этот матч.
        При чем ищется первое вхождение по любому из столбцов.
        :param player_name: Имя игрока для поиска в столбцах
            Player1 и Player2
        :param param_offset: Параметр для определения смещения страницы.
        :param param_limit: Параметр для обозначения лимита записей на странице.
        :return list_result: список с записями, где есть игрок
            c именем player_object_model в каждом из столбцов.
        """
        session = Session(bind=engine)

        try:
            # Получаем объект игрока из базы данных.
            # Получаем две записи из базы данных фильтруя их по СТОЛБЦАМ.
            player_object = session.query(Player).filter(Player.Name == player_name).one()
            select_target_matches_column_1 = session.query(Match).filter(Match.Player1 == player_object.ID,
                                                                         Match.Winner != None)
            select_target_matches_column_2 = session.query(Match).filter(Match.Player2 == player_object.ID,
                                                                         Match.Winner != None)

            # Объединяем записи для корректного отображения.
            union_result = select_target_matches_column_1.union_all(select_target_matches_column_2).\
                offset(param_offset).limit(param_limit).all()
            count_matches = select_target_matches_column_1.union_all(select_target_matches_column_2).\
                offset(param_offset).limit(param_limit).count()

            # Выполняем запрос result = session.execute(union_result).all() -
            # И формируем список с корректным результатом
            list_result = self.result_matches(union_result)

            # Выводим в консоль и возвращаем корректный список
            # self.output_console_list_result(list_result)
            return [list_result, count_matches]

        except ConnectionError:
            print("Connecting Error")

        finally:
            session.close()
            print("Session closed!")

    @staticmethod
    def select_by_id(record_id):
        session = Session(bind=engine)

        try:
            record_object = session.query(Match).filter(Match.ID == record_id).first()
            return record_object

        except ConnectionError:
            print("Connecting Error")

        finally:
            session.close()
            print("Session closed!")

    @staticmethod
    def select_last_record():
        """
        Получение последней записи из таблицы Matches
        :return: ID последней записи (ВНИМАНИЕ! Возвращается прям ID в
            виде целого ЧИСЛА, не ОБЪЕКТ)
        """
        session = Session(bind=engine)

        try:
            record_object = session.query(func.max(Match.ID)).scalar()
            # list_result = self.result_matches(record_object)

            # Выводим в консоль и возвращаем корректный список
            # self.output_console_list_result(list_result)
            return record_object

        except ConnectionError:
            print("Connecting Error")

        finally:
            session.close()
            print("Session closed!")
