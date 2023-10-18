import jinja2


def generate_sample_matches(all_matches, count_page_num, page_num, displayable_pages):
    """
    Метод генерирует шаблон веб страницы и отдаёт
    его пользователю.
    :param all_matches: Объект содержащий все матчи
    :param count_page_num: количество страниц пагинации для генерации динамичной страничек
    :param page_num: Номер страницы для дальнейшего постраничного переключения
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
    result_page = loading_page.render(all_match=all_matches,
                                      pages=page_num,
                                      page_number=count_page_num,
                                      )
    return result_page
