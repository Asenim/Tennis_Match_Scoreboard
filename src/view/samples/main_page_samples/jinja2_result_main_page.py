from src.view.samples.main_page_samples.jinja2_sample_main_page import generate_sample_main_page


def generate_result_main_page():
    result_page = generate_sample_main_page(
        displayable_pages='/main_page/page_main.html'
    )
    return result_page
