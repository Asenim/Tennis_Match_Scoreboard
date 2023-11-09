from src.view.samples.new_match_samples.jinja2_sample_new_match import generate_sample_new_match


def generate_result_new_match(your_ip):
    """
    :return:
    """
    result_page = generate_sample_new_match(
        your_ip=your_ip,
        displayable_pages='/new_match_page/page_new_match.html'
    )
    return result_page
