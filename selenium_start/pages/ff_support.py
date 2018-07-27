from selenium.webdriver.common.by import By
from .basepage import BasePage

class FfSupport(BasePage):

    _search_box_selector = (By.ID, 'search-q')
    _support_button_selector = (By.CSS_SELECTOR, '#get-involved-box .btn.btn-submit')

    """def __init__(self, selenium, variables, open_url=False):
        suffix_url = '/en-US/docs/Web/HTTP'
        super().__init__(selenium, variables, open_url, suffix_url)"""

    def confirm_page_load(self):
        self.is_visible(self._search_box_selector)

    def verify_support_button_is_clickable(self):
        return self.check_clickable(self._support_button_selector)