from selenium_start.pages.ff_support import FfSupport
from selenium_start.pages.header import Header
from selenium_start.pages.landing import LandingPage

def test_ffsupport_page(selenium, variables):
    LandingPage(selenium, variables, open_url=True)
    header = Header(selenium, variables)
    ffsupport = header.navigate_to_ff_support_page()
    assert ffsupport.verify_support_button_is_clickable()
