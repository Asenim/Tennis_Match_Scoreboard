from src.samples import jinja2_sample
from src.services.finished_matches_persistence_service.interaction_table_matches.select_interaction_table_matches \
    import SelectInteractionTableMatches


def generate_page_matches():
    """
    Генерирует статичную страницу
    с данными из таблицы.
    :return result: строка с данными из таблицы.
    """
    list_item = SelectInteractionTableMatches()
    results = list_item.select_all()
    result = jinja2_sample.generate_sample(results, '/matches_page/page_matches.html')
    return result
