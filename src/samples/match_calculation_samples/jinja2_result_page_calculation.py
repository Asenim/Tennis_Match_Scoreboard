from src.samples.match_calculation_samples.jinja2_sample_calculation \
    import generate_sample_calculation


def generate_result_page_calculation(player_1_score, player_2_score, id_match, ip_address):
    """
    Генерация страницы подсчета матча
    :param player_1_score: player_1_object: объект класса PlayerScore (Счета игрока 1)
    :param player_2_score: player_2_object: объект класса PlayerScore (Счета игрока 2)
    :param id_match: id текущего матча
    :param ip_address: IP ADDR из env
    """

    result_page = generate_sample_calculation(
        player_1_score, player_2_score, id_match, ip_address,
        '/match_score_page/match_score_calculation.html'
    )
    return result_page
