from src.samples.match_calculation_samples.jinja2_sample_calculation \
    import generate_sample_calculation
from src.services.finished_matches_persistence_service.interaction_table_players.select_table_players \
    import SelectInteractionTablePlayers


def generate_result_page_calculation(player_1_score, player_2_score):
    """
    Генерация страницы подсчета матча
    """

    result_page = generate_sample_calculation(
        player_1_score, player_2_score,
        '/match_score_page/match_score_calculation.html'
    )
    return result_page


