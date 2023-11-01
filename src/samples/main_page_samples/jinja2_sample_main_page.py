import jinja2


def generate_sample_main_page(displayable_pages):
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            '/app/src/pages'
        )
    )

    loading_page = env.get_template(displayable_pages)

    result_page = loading_page.render()
    return result_page
