"""Файл с точкой входа в программу"""
import wsgiref.handlers
import wsgiref.simple_server
import wsgiref.util
# Импорт шаблонов
from src.view.samples.new_match_samples import jinja2_result_new_match
from src.view.samples.main_page_samples import jinja2_result_main_page
# Импорт для работы роутинга
from src.services.server_configuration.match_score_url_conf import MatchScoreUrlConf
from src.services.server_configuration.matches_url_config import MatchesUrlConfig
from src.services.server_configuration.new_match_data_insert import NewMatchDataInsert
from src.services.server_configuration.match_score_data_handler import MatchScoreDataHandler
from config_env import YOUR_IP_ADDR


def application(env, start_response):
    string_url = wsgiref.util.request_uri(env, include_query=True)
    # Получение данных из Post Запроса
    # request_body = env.get('wsgi.input').read().decode('utf-8')
    request_body = env['wsgi.input'].read().decode('utf-8')
    print('----------')
    print('request_body', request_body)
    print('----------')
    url = string_url.split('/')[-1]

    # Главная страница
    if url == '':
        start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
        result_page = jinja2_result_main_page.generate_result_main_page()
        return [result_page.encode()]

    if url == 'style_main.css':
        start_response('200 OK', [('Content-Type', 'text/css;charset=utf-8')])
        with open('/app/src/view/pages/main_page/style_main.css', 'r') as index:
            reading = index.read()
            return [reading.encode('utf-8')]

    # Страница завершенных матчей
    get_url = url.split('?')
    match_url_config = MatchesUrlConfig(YOUR_IP_ADDR)
    if get_url[0] == 'matches':
        start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

        if len(get_url) == 1:
            result = match_url_config.page_formation_for_all_matches()
            return [result.encode('utf-8')]

        # Если есть get параметры
        elif len(get_url) > 1:
            get_param = get_url[1].split("&")

            # Если get param 1
            if len(get_param) == 1:
                get_data = get_param[0].split('=')

                if get_data[0] == 'page':
                    result = match_url_config.page_formation_for_all_matches(page=get_data[1])
                    return [result.encode('utf-8')]

                elif get_data[0] == 'filter_by_name':
                    # Если имя пустое
                    if get_data[1] == '':
                        start_response('302 Found', [('Location', f'/matches')])

                    result = match_url_config.page_formation_for_search_player(name=get_data[1])
                    return [result.encode('utf-8')]

            # Если get param 2 и более
            elif len(get_param) >= 2:
                # Достаем номер страницы
                get_data = get_param[0].split('=')
                # Достаем имя игрока по которому будем проводить поиск
                search_player = get_param[1].split('=')

                result = match_url_config.page_formation_for_search_player(page=get_data[1], name=search_player[1])
                return [result.encode('utf-8')]

    if url == 'matches_style.css':
        start_response('200 OK', [('Content-Type', 'text/css;charset=utf-8')])
        with open('/app/src/view/pages/matches_page/matches_style.css', 'r') as matches:
            reading = matches.read()
            return [reading.encode('utf-8')]

    # Страница нового матча
    if url == 'new-match':
        start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
        result_page = jinja2_result_new_match.generate_result_new_match(your_ip=YOUR_IP_ADDR)
        return [result_page.encode('utf-8')]

    if url == 'style_new_match.css':
        start_response('200 OK', [('Content-Type', 'text/css;charset=utf-8')])
        with open('/app/src/view/pages/new_match_page/style_new_match.css', 'r') as style_new_match:
            reading = style_new_match.read()
            return [reading.encode('utf-8')]

    # Страница подсчета матча
    get_url = url.split('?')
    if get_url[0] == 'match_score':
        start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
        # Получаем get параметр (ID Матча)
        get_parameter = get_url[1].split('=')
        id_matches = get_parameter[1]

        match_score_url_conf = MatchScoreUrlConf(YOUR_IP_ADDR)

        result_page = match_score_url_conf.page_formation_for_match_score(id_matches)
        return [result_page.encode('utf-8')]

    if url == 'style_match_score_calculation.css':
        start_response('200 OK', [('Content-Type', 'text/css;charset=utf-8')])
        with open('/app/src/view/pages/match_score_page/style_match_score_calculation.css', 'r') as style_score_match:
            reading = style_score_match.read()
            return [reading.encode('utf-8')]

    # Обработка данных со страницы начала матча
    if url == 'new_match_data_insert':
        print(get_url)
        start_new_match_data_insert = NewMatchDataInsert()
        id_matches = start_new_match_data_insert.treatment_new_match_data(request_body)

        # Производим redirect
        start_response('302 Found', [('Location', f'/match_score?uuid={id_matches}')])

    # Обработка данных со страницы подсчета матча
    if url == 'match_score_data_handler':
        # Парсим полученную строку с именами
        str_request_body = str(request_body)
        # Убираем лишние символы из строки и разбиваем ее
        post_data = str_request_body.replace("'", "").split('&')
        start_match_score_data_handler = MatchScoreDataHandler()
        list_data = start_match_score_data_handler.treatment_match_score_data(post_request_data=post_data)
        score_player_1_object = list_data[0]
        score_player_2_object = list_data[1]
        id_current_match = list_data[2]
        # Производим redirect
        # Если выиграл игрок 1
        if score_player_1_object.game_set >= 3:
            start_match_score_data_handler.redirect_win_conf(id_current_match, score_player_1_object,
                                                             score_player_2_object, score_player_1_object)
            start_response('302 Found', [('Location', f"/matches?page=1")])

        # Если выиграл игрок 2
        elif score_player_2_object.game_set >= 3:
            start_match_score_data_handler.redirect_win_conf(id_current_match, score_player_1_object,
                                                             score_player_2_object, score_player_2_object)
            start_response('302 Found', [('Location', f"/matches?page=1")])

        # Пока никто не выиграл
        else:
            start_match_score_data_handler.redirect_not_win_conf(id_current_match, score_player_1_object,
                                                                 score_player_2_object)
            start_response('302 Found', [('Location', f'/match_score?uuid={id_current_match}')])

    if url not in ['match_score_data_handler', 'new_match_data_insert',
                   'style_match_score_calculation.css', 'match_score',
                   'style_new_match.css', 'new-match', 'matches_style.css',
                   'matches', 'style_main.css', '']:
        page_not_found = '404, Страницы не существует'
        start_response('404 Not Found', [('Content-Type', 'text/plain;charset=utf-8')])
        return [page_not_found.encode('utf-8')]
