"""Файл с точкой входа в программу"""
import wsgiref.util, wsgiref.handlers, wsgiref.simple_server
# Импорт шаблонов
from src.samples.result_matches_samples import jinja2_result_page_matches
from src.samples.new_match_samples import jinja2_result_new_match
from src.samples.match_calculation_samples import jinja2_result_page_calculation
# Импорт сервисов для работы с БД
from src.services.ongoing_matches_service.ongoing_matches_service import OngoingMatchesService
from src.services.finished_matches_persistence_service.interaction_table_players.select_table_players \
    import SelectInteractionTablePlayers
from src.services.finished_matches_persistence_service.interaction_table_matches.insert_table_matches \
    import InsertTableMatches
from src.services.finished_matches_persistence_service.interaction_table_matches.object_to_json_to_db \
    import ObjectToJsonToDB
from src.services.finished_matches_persistence_service.interaction_table_matches.select_table_matches \
    import SelectTableMatches
# Импорт сервисов логики приложения
from src.services.match_score_calculation_service.match_score_logic.player_score import PlayerScore
from src.services.match_score_calculation_service.coolbus_setup import CoolBusSetUp
# Прочие воспомогательные модули
import math


def application(env, start_response):
    string_url = wsgiref.util.request_uri(env, include_query=True)
    # Получение данных из Post Запроса
    request_body = env.get('wsgi.input').read()
    print('----------')
    print('request_body', request_body)
    print('----------')
    url = string_url.split('/')[-1]

    # Главная страница
    if url == '':
        start_response('200 OK', [('Content-Type', 'text/html')])
        with open('/app/src/pages/main_page/page_main.html', 'r') as index:
            reading = index.read()
            return [reading.encode()]

    if url == 'style_main.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        with open('/app/src/pages/main_page/style_main.css', 'r') as index:
            reading = index.read()
            return [reading.encode()]

    # Страница завершенных матчей
    get_url = url.split('?')
    if get_url[0] == 'matches':
        start_response('200 OK', [('Content-Type', 'text/html')])

        get_response = get_url[1].split("&")
        if len(get_response) == 1:
            page_number = get_response[0].split('=')
            int_page_num = int(page_number[1])

            # Номер страницы
            page = 0 + int_page_num
            if page <= 0:
                page = 1
            # Количество записей на одну страницу
            quantity_per_page = 1
            # Определяем смещение и лимит для запроса пагинации
            offset = (page - 1) * quantity_per_page
            start_select_matches = SelectTableMatches()

            # Получаем записи из БД
            all_matches_and_count_all_match = start_select_matches.select_all(param_offset=offset,
                                                                              param_limit=quantity_per_page)
            all_matches = all_matches_and_count_all_match[0]
            count_matches = all_matches_and_count_all_match[1]
            # Количество страниц необходимое для отображения всех матчей
            quantity_pages = math.ceil(count_matches / quantity_per_page)

            result = jinja2_result_page_matches.generate_result_page_matches(results=all_matches,
                                                                             count_number=quantity_pages,
                                                                             page_num=page)

            return [result.encode()]
        elif len(get_response) >= 2:
            # Достаем номер страницы
            page_number = get_response[0].split('=')
            int_page_num = int(page_number[1])
            # Достаем имя игрока по которому будем проводить поиск
            search_player = get_response[1].split('=')
            player_name_is_url = search_player[1]
            start_select_matches = SelectTableMatches()
            # Номер страницы
            page = 0 + int_page_num
            # Количество записей на одну страницу
            quantity_per_page = 2
            # Определяем смещение и лимит для запроса пагинации
            offset = (page - 1) * quantity_per_page
            start_select_matches = SelectTableMatches()

            all_matches = start_select_matches.selection_by_one_name(player_name_is_url,
                                                                     offset, quantity_per_page)

            result = jinja2_result_page_matches.generate_result_page_matches(results=all_matches,
                                                                             count_number=quantity_per_page,
                                                                             page_num=page)

            return [result.encode()]

    if url == 'matches_style.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        with open('/app/src/pages/matches_page/matches_style.css', 'r') as matches:
            reading = matches.read()
            return [reading.encode()]

    # Страница нового матча
    if url == 'new-match':
        start_response('200 OK', [('Content-Type', 'text/html')])
        """
        Добавить возмодность начинать матч если имя которое уже есть в БД 
        отправляется еще раз
        """

        result_page = jinja2_result_new_match.generate_result_new_match()
        return [result_page.encode()]

    if url == 'style_new_match.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        with open('/app/src/pages/new_match_page/style_new_match.css', 'r') as style_new_match:
            reading = style_new_match.read()
            return [reading.encode()]

    # Страница подсчета матча
    get_url = url.split('?')
    if get_url[0] == 'match_score':
        start_response('200 OK', [('Content-Type', 'text/html')])
        # Получаем get параметр (ID Матча)
        get_parameter = get_url[1].split('=')
        id_matches = get_parameter[1]

        # Получаем объекты игроков текущего матча
        start_class_select_matches = SelectTableMatches()
        start_class_select_players = SelectInteractionTablePlayers()
        match_record = start_class_select_matches.select_by_id(id_matches)
        player_1_id = match_record.Player1
        player_2_id = match_record.Player2
        player_1_object = start_class_select_players.select_one_player(player_id=player_1_id)
        player_2_object = start_class_select_players.select_one_player(player_id=player_2_id)

        # Получаем данные счета из json
        run_class_object_to_json = ObjectToJsonToDB()
        get_data_in_python_is_json = run_class_object_to_json.db_str_to_dict(id_matches)
        score_player_1 = get_data_in_python_is_json[0]
        score_player_2 = get_data_in_python_is_json[1]
        # Создаём объекты для отрисовки
        player1_obj_score = PlayerScore(player_1_object, score_player=score_player_1)
        player2_obj_score = PlayerScore(player_2_object, score_player=score_player_2)

        result_page = jinja2_result_page_calculation.generate_result_page_calculation(
            player1_obj_score, player2_obj_score, id_matches
        )

        return [result_page.encode()]

    if url == 'style_match_score_calculation.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        with open('/app/src/pages/match_score_page/style_match_score_calculation.css', 'r') as style_score_match:
            reading = style_score_match.read()
            return [reading.encode()]

    # Обработка данных со страницы начала матча
    if url == 'new_match_data_insert':
        print(get_url)
        list_player_objects = post_new_match_handler(request_body=request_body)
        print('p1, p2, id match', list_player_objects)
        player1_obj = list_player_objects[0]
        player2_obj = list_player_objects[1]
        id_matches = list_player_objects[2]

        # Создаются объекты подсчета матча
        player1_obj_score = PlayerScore(player1_obj)
        player2_obj_score = PlayerScore(player2_obj)
        # Данные переводятся в формат json
        run_class_object_to_json = ObjectToJsonToDB(player1_obj_score, player2_obj_score)
        data_object_to_json = run_class_object_to_json.object_to_json()
        print(data_object_to_json)
        print(type(data_object_to_json))
        # Обновляются данные в БД
        update_matches_score = InsertTableMatches()
        update_matches_score.update_score_match(id_matches, data_object_to_json)

        # Производим redirect
        start_response('302 Found', [('Location', f'/match_score?uuid={id_matches}')])

    # Обработка данных со страницы подсчета матча
    if url == 'match_score_data_handler':
        # Парсим полученную строку с именами
        str_request_body = str(request_body)
        # Убираем лишние символы из строки и разбиваем ее
        post_data = str_request_body.replace("'", "").split('&')
        print(post_data)
        # Получаем id текущего матча
        key_value_id_match = post_data[0].split('=')
        id_current_match = key_value_id_match[1]
        # Получаем номер победившего игрока
        key_value_player = post_data[1].split('=')
        num_win_player = key_value_player[1]

        # Достаем ID игроков из таблицы матча
        run_class_select_table_matches = SelectTableMatches()
        record_table_matches = run_class_select_table_matches.select_by_id(id_current_match)
        id_player_1 = record_table_matches.Player1
        id_player_2 = record_table_matches.Player2
        print('id_players', id_player_1, id_player_2)
        # Достаем самих игроков из таблицы игроков
        run_class_select_players = SelectInteractionTablePlayers()
        player_1_object = run_class_select_players.select_one_player(player_id=id_player_1)
        player_2_object = run_class_select_players.select_one_player(player_id=id_player_2)
        print('player_object', player_1_object.Name, player_2_object.Name)
        # Получаем текущий счет
        run_class_object_to_json = ObjectToJsonToDB()
        current_score = run_class_object_to_json.db_str_to_dict(id_current_match)
        player_1_score = current_score[0]
        player_2_score = current_score[1]
        print(player_1_score, player_2_score)

        # Запускаем логику приложения, меняем счет игроков и возвращаем объекты игроков
        run_class_coolbus_setup = CoolBusSetUp(id_match=id_current_match,
                                               player1_object_model=player_1_object,
                                               player2_object_model=player_2_object,
                                               player1_score=player_1_score,
                                               player2_score=player_2_score,
                                               point_win_request=num_win_player)

        start_count_score = run_class_coolbus_setup.start_counting_score()
        score_player_1_object = start_count_score[0]
        score_player_2_object = start_count_score[1]
        run_new_data_is_object_to_json = ObjectToJsonToDB(score_player_1_object, score_player_2_object)
        run_class_insert_table_matches = InsertTableMatches()

        # Производим redirect
        if score_player_1_object.game_set >= 3:

            new_json_data = run_new_data_is_object_to_json.object_to_json()
            run_class_insert_table_matches.update_score_match(id_current_match, new_json_data)

            run_class_insert_table_matches.insert_winner_player_id(id_current_match, score_player_1_object.player_ID)
            start_response('302 Found', [('Location', f"/matches")])

        elif score_player_2_object.game_set >= 3:
            new_json_data = run_new_data_is_object_to_json.object_to_json()
            run_class_insert_table_matches.update_score_match(id_current_match, new_json_data)

            run_class_insert_table_matches.insert_winner_player_id(id_current_match, score_player_2_object.player_ID)
            start_response('302 Found', [('Location', f"/matches")])

        else:
            new_json_data = run_new_data_is_object_to_json.object_to_json()
            run_class_insert_table_matches.update_score_match(id_current_match, new_json_data)

            start_response('302 Found', [('Location', f'/match_score?uuid={id_current_match}')])


def post_new_match_handler(request_body):
    """
    Обработка POST запроса из страницы нового матча
    :param request_body: для парсинга данных из тела запроса.
    :return: Список с объектами игроков из БД и с ID матча
    """
    # Парсим полученную строку с именами
    str_request_body = str(request_body)
    # Убираем лишние символы из строки и разбиваем ее
    post_data = str_request_body.replace("'", "").split('&')
    # Отделяем игроков друг от друга для дальнейшей обработки
    post_data_player_1 = post_data[0]
    post_data_player_2 = post_data[1]
    # ong = OngoingMatchesService()
    print('post_data', post_data, 'player_1', post_data_player_1, 'player_2', post_data_player_2)
    # Вытаскиваем имена игроков
    # Разбиваем строку с именами игроков
    list_player_1 = post_data_player_1.split('=')
    list_player_2 = post_data_player_2.split('=')
    # Вытаскиваем из списков имена и убираем лишние пробелы
    player_1 = list_player_1[1].replace(' ', '')
    player_2 = list_player_2[1].replace(' ', '')
    # Добавляем игроков в Таблицу Players
    ongoing = OngoingMatchesService(player_1, player_2)
    ongoing.insert_in_table_players()
    # Извлекаем игроков из таблицы Player для получения их id
    player1_obj_query = SelectInteractionTablePlayers()
    player_1_obj = player1_obj_query.select_one_player(player_1)
    player2_obj_query = SelectInteractionTablePlayers()
    player_2_obj = player2_obj_query.select_one_player(player_2)
    # Отправляем Игроков в таблицу Matches
    insert_players_in_match_table = InsertTableMatches()
    id_insert_match = insert_players_in_match_table.insert_matches(player_1_obj.ID, player_2_obj.ID)
    print('insert_data_obj', id_insert_match, dir(id_insert_match))

    return [
        player_1_obj,
        player_2_obj,
        id_insert_match
            ]


def post_match_score_handler(request_body):
    pass
