from src.view.samples.result_matches_samples import jinja2_sample_matches


def generate_result_page_matches(results, count_number, page_num, pl_name, your_ip):
    """
    Генерирует статичную страницу
    с данными из таблицы.
    :return result: строка с данными из таблицы.
    """

    result = jinja2_sample_matches.generate_sample_matches(all_matches=results, count_page_num=count_number,
                                                           page_num=page_num, player_name=pl_name, your_ip=your_ip,
                                                           displayable_pages='/matches_page/page_matches.html')
    return result
