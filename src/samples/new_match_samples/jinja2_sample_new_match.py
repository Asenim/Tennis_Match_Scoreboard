import jinja2


def generate_sample_new_match(displayable_pages):
    """
    Метод генерирует шаблон веб страницы и отдаёт
    его пользователю.
    :param displayable_pages: Сама отображаемая страница.
        /app/src/pages
    :return:
    """
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            '/app/src/pages'
        )
    )

    loading_page = env.get_template(displayable_pages)
    # my_object - это имя объекта в html странице который будет отображаться
    # с помощью шаблонизатора.
    result_page = loading_page.render()
    return result_page
