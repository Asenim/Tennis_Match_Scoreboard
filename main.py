"""Файл с точкой входа в программу"""
import wsgiref.util


def application(env, start_response):
    string_url = wsgiref.util.request_uri(env, include_query=True)

    print(string_url)
    url = string_url.split('/')[-1]
    print(url)

    # Главная страница
    if url == '':
        start_response('200 OK', [('Content-Type', 'text/html')])
        with open('/home/alfob/Tennis_ball_scoreboard/pages/main_page/page_main.html', 'r') as index:
            reading = index.read()
            return [reading.encode()]

    # Стили главной страницы
    if url == 'style_main.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        with open('/home/alfob/Tennis_ball_scoreboard/pages/main_page/style_main.css', 'r') as index:
            reading = index.read()
            return [reading.encode()]

    if url == 'matches':
        start_response('200 OK', [('Content-Type', 'text/html')])
        with open('/home/alfob/Tennis_ball_scoreboard/pages/matches_page/page_matches.html', 'r') as matches:
            reading = matches.read()
            return [reading.encode()]

    if url == 'matches_style.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        with open('/home/alfob/Tennis_ball_scoreboard/pages/matches_page/matches_style.css', 'r') as matches:
            reading = matches.read()
            return [reading.encode()]
