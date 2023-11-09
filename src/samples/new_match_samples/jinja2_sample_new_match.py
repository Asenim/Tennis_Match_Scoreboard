import jinja2


def generate_sample_new_match(your_ip, displayable_pages):
    """
    Метод генерирует шаблон веб страницы и отдаёт
    его пользователю.
    :param your_ip: IP из .env
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
    result_page = loading_page.render(your_ip=your_ip)
    return result_page
