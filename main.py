"""Файл с точкой входа в программу"""
import wsgiref.util, wsgiref.handlers
# from src.samples import jinja2_sample
from src.samples import jinja2_result_page_matches
from src.services.ongoing_matches_service.ongoing_matches_service import OngoingMatchesService


def application(env, start_response):
    string_url = wsgiref.util.request_uri(env, include_query=True)
    # item1 = wsgiref.util.application_uri(env)
    # envi = env
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

        result = jinja2_result_page_matches.generate_page_matches()
        return [result.encode()]

    if url == 'matches_style.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        with open('/app/src/pages/matches_page/matches_style.css', 'r') as matches:
            reading = matches.read()
            return [reading.encode()]

    if url == 'new-match':
        if env['REQUEST_METHOD'] == 'POST':
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
            print("*****")
            print(player_1, player_2)
            print('*****')
            # Добавляем игроков в базу данных
            ongoing = OngoingMatchesService(player_1, player_2)
            ongoing.insert_in_table_players()
        start_response('200 OK', [('Content-Type', 'text/html')])
        with open('/app/src/pages/new_match_page/page_new_match.html', 'r') as new_match:
            reading = new_match.read()
            return [reading.encode()]

    if url == 'style_new_match.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        with open('/app/src/pages/new_match_page/style_new_match.css', 'r') as style_new_match:
            reading = style_new_match.read()
            return [reading.encode()]
