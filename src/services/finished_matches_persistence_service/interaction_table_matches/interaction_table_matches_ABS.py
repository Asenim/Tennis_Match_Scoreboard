from src.services.finished_matches_persistence_service.interaction_table_ABS \
    import InteractionTableABS


class InteractionTableMatchesABS(InteractionTableABS):
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
            list_add_in_list_result = [
                select.player1.Name,
                select.player2.Name,
                select.winner.Name]
            list_result.append(list_add_in_list_result)
        return list_result
