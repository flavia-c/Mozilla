from selenium.webdriver.common.by import By
from .basepage import BasePage

class Html(BasePage):

    _settings_icon_selector = (By.CLASS_NAME, 'icon-cog')
    _title_header_locator = (By.TAG_NAME, 'h1')
    _html_page_title = "HTML"
    _html_page_suffix = '/en-US/docs/Web/HTML'

    def __init__(self, selenium, variables, open_url=False):
        super().__init__(selenium=selenium,
                         variables=variables,
                         open_url=open_url,
                         suffix_url=self._html_page_suffix
                         )

    def confirm_page(self):
        self.text_is_present_in_element(
            self._title_header_locator,
            self._html_page_title
        )

    def check_settings_button_clickable(self):
        return self.check_clickable(self._settings_icon_selector)
