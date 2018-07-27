from selenium.webdriver.common.by import By
from .basepage import BasePage

class DevTools(BasePage):

    _devtools_page_suffix = '/en-US/docs/Tools'

    _title_header_locator = (By.TAG_NAME, 'h1')
    _tools_page_title = 'Firefox Developer Tools'

    _core_tools_selector = (By.LINK_TEXT, 'The Core Tools')
    _languages_button_selector = (By.ID, '#languages-menu')
    _core_tools_dropdown_selector = (By.XPATH, '//div[@id="Subnav"]/ol/li[1]/a')
    _search_button_selector = (By.CLASS_NAME, '.icon-search')
    _web_console_selector = (By.CSS_SELECTOR, 'p a[href$="/en-US/docs/Tools/Web_Console"]')

    def __init__(self, selenium, variables, open_url):
        super().__init__(selenium=selenium,
                         variables=variables,
                         open_url=open_url,
                         suffix_url=self._devtools_page_suffix)

    def confirm_page_load(self):
        self.text_is_present_in_element(
            self._title_header_locator,
            self._tools_page_title
        )

    def core_tools_button_is_enabled(self):
        return self.check_clickable(self._core_tools_selector)

    def web_console_is_visible(self):
        return self.is_visible(self._web_console_selector)





