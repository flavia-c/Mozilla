import pytest

from selenium_start.pages.landing import LandingPage
from ..pages.header import Header
from ..pages.http import Http
from ..pages.html import Html


def test_mozilla_search(selenium, variables):
    landing_page = LandingPage(selenium, variables, open_url=True)
    landing_page.search('firefox')
    assert selenium.title == 'Search Results for "firefox" | MDN'


@pytest.mark.xfail
def test_mozilla_search_fail(selenium, variables):
    landing_page = LandingPage(selenium, variables, open_url=True)
    search_results = landing_page.search('aer conditionat')
    search_results.click_second_result()
    assert 'caca' in selenium.title

def test_navigate_to_http_page(selenium, variables):
    LandingPage(selenium, variables, open_url=True)
    header = Header(selenium, variables)
    http = header.navigate_to_http_page()
    assert http.edit_button_is_enabled()

def test_edit_button_is_enabled_on_http_page(selenium, variables):
    http = Http(selenium, variables, open_url=True)
    assert http.edit_button_is_enabled()


