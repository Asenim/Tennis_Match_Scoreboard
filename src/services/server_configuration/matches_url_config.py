from src.services.finished_matches_persistence_service.interaction_table_matches.select_table_matches \
    import SelectTableMatches
import math
from src.view.samples.result_matches_samples import jinja2_result_page_matches


class MatchesUrlConfig:
    def __init__(self, ip_addr):
        """
        Этот класс нужен для конфигурации url
        /matches, а точнее для обратки get аргументов и
        формирования страниц
        """
        self.start_select_matches = SelectTableMatches()
        self.IP_ADDR = ip_addr

    def page_formation_for_all_matches(self, page=None):
        """
        Метод формирует страницу с сыгранными матчами всех игроков
        :param page: -> None/str Количество страниц/Номер страницы
        :return result: это строка с шаблоном страницы который будет отображаться
            в браузере.
        """
        if page is None:
            data_for_pages = self.page_formation_with_pagination()
        else:
            data_for_pages = self.page_formation_with_pagination(page_num=page)
        # Получаем данные из БД
        all_matches_and_count_all_match = self.start_select_matches.select_all(param_offset=data_for_pages['offset'],
                                                                               param_limit=data_for_pages['quantity_per_page'])
        all_matches = all_matches_and_count_all_match[0]
        count_matches = all_matches_and_count_all_match[1]
        # Количество страниц необходимое для отображения всех матчей
        quantity_pages = math.ceil(count_matches / data_for_pages['quantity_per_page'])

        result = jinja2_result_page_matches.generate_result_page_matches(results=all_matches,
                                                                         count_number=quantity_pages,
                                                                         page_num=data_for_pages['page'],
                                                                         pl_name=data_for_pages['name'],
                                                                         your_ip=self.IP_ADDR)

        return result

    def page_formation_for_search_player(self, page='1', name=''):
        """
        Метод формирует страницу с сыгранными матчами игроков которые
        были введены в поле поиска в браузере
        :param page: -> str Должен получать на вход номер страницы
        :param name: -> str Должен получать на вход имя игрока
        :return result: это строка с шаблоном страницы который будет отображаться
            в браузере.
        """
        data_for_pages = self.page_formation_with_pagination(page_num=page, player_name=name)

        search_matches_and_count_all_match = self.start_select_matches.selection_by_one_name(data_for_pages['name'],
                                                                                             data_for_pages['offset'],
                                                                                             data_for_pages['quantity_per_page'])
        # # Получаем записи из БД
        all_matches = search_matches_and_count_all_match[0]
        count_matches = search_matches_and_count_all_match[1]
        # Количество страниц необходимое для отображения всех матчей
        quantity_pages = math.ceil(count_matches / data_for_pages['quantity_per_page'])

        result = jinja2_result_page_matches.generate_result_page_matches(results=all_matches,
                                                                         count_number=quantity_pages,
                                                                         page_num=data_for_pages['page'],
                                                                         pl_name=data_for_pages['name'],
                                                                         your_ip=self.IP_ADDR)
        return result

    @staticmethod
    def page_formation_with_pagination(page_num='1', player_name=''):
        """
        Функция позволяет формировать словарь с данными которые в
            дальнейшем служат для формирования страниц и пагинации.
        :param page_num: -> str Должен получать на вход номер страницы
        :param player_name: -> str Должен получать на вход имя игрока
        :return data_for_insertion: -> dict Возвращает словарь с полями
            {
            'page': Номер страницы,
            'name': Имя искомого игрока,
            'quantity_per_page': Количество записей на одну страницу,
            'offset': Смещение для запроса пагинации
            }
        """
        # Номер страницы
        int_page_num = int(page_num)
        page = 0 + int_page_num
        if page <= 0:
            page = 1
        # Имя игрока
        name = player_name

        # Количество записей на одну страницу
        quantity_per_page = 5
        # Определяем смещение для запроса пагинации
        offset = (page - 1) * quantity_per_page

        data_for_insertion = {
            'page': page,
            'name': name,
            'quantity_per_page': quantity_per_page,
            'offset': offset
        }

        return data_for_insertion
