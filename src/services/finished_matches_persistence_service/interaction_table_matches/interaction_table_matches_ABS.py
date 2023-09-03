from src.services.finished_matches_persistence_service.interaction_table_ABS \
    import InteractionTableABS
# import json


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
            list_add_in_list_result = [select.player1.Name,
                                       select.player2.Name,
                                       select.winner.Name]
            list_result.append(list_add_in_list_result)
        return list_result


if "__main__" == __name__:
    pass
    # matches = InteractionTableMatches()
    # print(matches.select_matches(name_p1='Alfob'))
    # print('----')
    # print(matches.select_matches())
    # matches.select_matches(name_p1='Sergey')
    # matches.select_matches(name_p1='Sergey', name_p2='Alfob')
    # matches.insert_matches(4, 5, 4)
    # matches.insert_matches(5, 6, 5)
    # matches.insert_matches(6, 4, 4)
    # matches.insert_matches(4, 7, 4)
    # matches.insert_matches(4, 8, 4)
    # matches.insert_matches(4, 9, 4)
    # matches.insert_matches(4, 10, 4)
