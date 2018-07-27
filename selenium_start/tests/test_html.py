from selenium_start.pages.html import Html

def test_html_page(selenium, variables):
    html = Html(selenium=selenium, variables=variables, open_url=True)
    assert html.check_settings_button_clickable()