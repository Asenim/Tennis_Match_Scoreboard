import jinja2


def generate_sample_calculation(player_1_object, player_2_object, id_match, your_ip, displayable_pages):
    """
    Метод Вставляет необходимые данные в шаблон страницы
    и отдает результат
    :param player_1_object: объект класса PlayerScore (Счета игрока 1)
    :param player_2_object: объект класса PlayerScore (Счета игрока 2)
    :param id_match: id текущего матча
    :param your_ip: IP из файла .env
    :param displayable_pages: Сама отображаемая страница.
        /app/src/pages
    :return:
    """
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            '/app/src/view/pages'
        )
    )
    """ Идея - обратиться к полям объекта игроков и пердавать даные полей """
    loading_page = env.get_template(displayable_pages)

    # Возможные варианты шапок подсчета матча
    tie_break_hand = 'TieBreak'
    game_hand = 'Game'

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
    if p1_score == 40 and p2_score == 40:
        result_page = loading_page.render(p1_dis_name=p1_name,
                                          p1_dis_score="AD",
                                          p1_dis_game=p1_game,
                                          p1_dis_set=p1_set,
                                          p2_dis_name=p2_name,
                                          p2_dis_score="AD",
                                          p2_dis_game=p2_game,
                                          p2_dis_set=p2_set,
                                          id=id_match,
                                          handler_game=game_hand,
                                          your_ip=your_ip
                                          )

    elif p1_game == 6 and p2_game == 6:
        result_page = loading_page.render(p1_dis_name=p1_name,
                                          p1_dis_score=p1_score,
                                          p1_dis_game=p1_tiebreak,
                                          p1_dis_set=p1_set,
                                          p2_dis_name=p2_name,
                                          p2_dis_score=p2_score,
                                          p2_dis_game=p2_tiebreak,
                                          p2_dis_set=p2_set,
                                          id=id_match,
                                          handler_game=tie_break_hand,
                                          your_ip=your_ip
                                          )

    else:
        result_page = loading_page.render(p1_dis_name=p1_name,
                                          p1_dis_score=p1_score,
                                          p1_dis_game=p1_game,
                                          p1_dis_set=p1_set,
                                          p2_dis_name=p2_name,
                                          p2_dis_score=p2_score,
                                          p2_dis_game=p2_game,
                                          p2_dis_set=p2_set,
                                          id=id_match,
                                          handler_game=game_hand,
                                          your_ip=your_ip
                                          )

    return result_page
