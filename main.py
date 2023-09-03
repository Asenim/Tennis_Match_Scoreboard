"""Файл с точкой входа в программу"""
import wsgiref.util
from src.samples import jinja2_sample
from src.samples import jinja2_result_page_matches


def application(env, start_response):
    string_url = wsgiref.util.request_uri(env, include_query=True)

    print(string_url)
    url = string_url.split('/')[-1]
    print(url)

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
        # list item будет убраться, Тут будет информация из БД,
        # которая будет передаваться первым аргументом в мой генератор шаблона

        # list_item = InteractionTableMatches()
        # results = list_item.select_matches()
        # results = [[1, 2], [2, 3], [3, 4]]
        # result = jinja2_sample.generate_sample(results, '/matches_page/page_matches.html')
        result = jinja2_result_page_matches.generate_page_matches()
        return [result.encode()]

    if url == 'matches_style.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        with open('/app/src/pages/matches_page/matches_style.css', 'r') as matches:
            reading = matches.read()
            return [reading.encode()]
