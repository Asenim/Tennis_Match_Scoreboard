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
# Импорт сервисов логики приложения
from src.services.match_score_calculation_service.match_score_logic.player_score import PlayerScore


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

    # Стили главной страницы
    if url == 'style_main.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        with open('/app/src/pages/main_page/style_main.css', 'r') as index:
            reading = index.read()
            return [reading.encode()]

    if url == 'matches':
        start_response('200 OK', [('Content-Type', 'text/html')])

        result = jinja2_result_page_matches.generate_result_page_matches()
        return [result.encode()]

    if url == 'matches_style.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        with open('/app/src/pages/matches_page/matches_style.css', 'r') as matches:
            reading = matches.read()
            return [reading.encode()]

    if url == 'new-match':
        start_response('200 OK', [('Content-Type', 'text/html')])

        result_page = jinja2_result_new_match.generate_result_new_match()
        return [result_page.encode()]

    if url == 'style_new_match.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        with open('/app/src/pages/new_match_page/style_new_match.css', 'r') as style_new_match:
            reading = style_new_match.read()
            return [reading.encode()]

    get_url = url.split('?')
    if get_url[0] == 'match_score':

        result_page = jinja2_result_page_calculation.generate_result_page_calculation(
            player1_obj_score, player2_obj_score
        )

        return [result_page.encode()]

    if url == 'style_match_score_calculation.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        with open('/app/src/pages/match_score_page/style_match_score_calculation.css', 'r') as style_score_match:
            reading = style_score_match.read()
            return [reading.encode()]

    if url == 'new_match_data_insert':
        print(env)
        start_response('200 OK', [('Content-Type', 'text/html')])
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
    # # Обновляем данные счета матча в БД
    # player1_obj_score = PlayerScore(player_1_obj)
    # player2_obj_score = PlayerScore(player_2_obj)
    # object_to_json = ObjectToJsonToDB(player1_obj_score, player2_obj_score)
    # insert_players_in_match_table.update_score_match(id_insert_match, object_to_json)

    return [
        player_1_obj,
        player_2_obj,
        id_insert_match
            ]
