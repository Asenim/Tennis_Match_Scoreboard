from src.samples.result_matches_samples import jinja2_sample_matches
from src.services.finished_matches_persistence_service.interaction_table_matches.select_table_matches \
    import SelectTableMatches


def generate_result_page_matches():
    """
    Генерирует статичную страницу
    с данными из таблицы.
    :return result: строка с данными из таблицы.
    """
    list_item = SelectTableMatches()
    results = list_item.select_all()
    result = jinja2_sample_matches.generate_sample_matches(results, '/matches_page/page_matches.html')
    return result
