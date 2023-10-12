import jinja2


def generate_sample_calculation(player_1_object, player_2_object, id_match, displayable_pages):
    """
    Метод Вставляет необходимые данные в шаблон страницы
    и отдает результат
    :param player_1_object: объект класса PlayerScore (Счета игрока 1)
    :param player_2_object: объект класса PlayerScore (Счета игрока 2)
    :param id_match: id текущего матча
    :param displayable_pages: Сама отображаемая страница.
        /app/src/pages
    :return:
    """
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            '/app/src/pages'
        )
    )
    """ Идея - обратиться к полям объекта игроков и пердавать даные полей """
    loading_page = env.get_template(displayable_pages)

    # Получаем данные игрока номер 1
    p1_name = player_1_object.player_name
    p1_score = player_1_object.score
    p1_game = player_1_object.game
    p1_set = player_1_object.game_set
    p1_tiebreak = player_1_object.tie_break

    # Получаем данные игрока номер 2
    p2_name = player_2_object.player_name
    p2_score = player_2_object.score
    p2_game = player_2_object.game
    p2_set = player_2_object.game_set
    p2_tiebreak = player_2_object.tie_break

    # dis - это имя объекта в html странице который будет отображаться
    # с помощью шаблонизатора.
    result_page = loading_page.render(p1_dis_name=p1_name,
                                      p1_dis_score=p1_score,
                                      p1_dis_game=p1_game,
                                      p1_dis_set=p1_set,
                                      p1_dis_tiebreak=p1_tiebreak,
                                      p2_dis_name=p2_name,
                                      p2_dis_score=p2_score,
                                      p2_dis_game=p2_game,
                                      p2_dis_set=p2_set,
                                      p2_dis_tiebreak=p2_tiebreak,
                                      id=id_match
                                      )
    return result_page
