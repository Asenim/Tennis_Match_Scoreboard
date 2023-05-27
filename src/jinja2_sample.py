import jinja2


def generate_sample(displayable_data, displayable_pages):
    """
    Метод генерирует шаблон веб страницы и отдаёт
    его пользователю.
    :param displayable_data: Объект, который будет отображаться
        на странице.
    :param displayable_pages: Сама отображаемая страница.
        /home/alfob/Tennis_ball_scoreboard/pages
    :return:
    """
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            "/home/alfob/Tennis_ball_scoreboard/pages"
        )
    )

    loading_page = env.get_template(displayable_pages)
    # my_object - это имя объекта в html странице который будет отображаться
    # с помощью шаблонизатора.
    result_page = loading_page.render(my_object=displayable_data)
    return result_page
