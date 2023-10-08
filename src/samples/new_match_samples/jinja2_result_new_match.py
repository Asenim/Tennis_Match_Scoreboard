from src.samples.new_match_samples.jinja2_sample_new_match import generate_sample_new_match


def generate_result_new_match():
    """
    Предстоящая работа:
    Здесь должна вставляться информация о начале матча
    в таблицу matches
    Далее извлекаться последняя вставленная в БД запись из
    таблицы matches
    Затем получать id последней записи в бд Matches.
    вставлять этот ID в url

    :return:
    """
    id_match = 'id_matches'
    result_page = generate_sample_new_match(
        displayable_data=id_match,
        displayable_pages='/new_match_page/page_new_match.html'
    )
    return result_page
