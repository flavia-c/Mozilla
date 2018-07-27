""" Page Object Class for the landing page for Mozilla Developers site"""

from selenium.webdriver.common.by import By

from .basepage import BasePage
from .search_results import SearchResultsPage
from .dev_tools import DevTools

class LandingPage(BasePage):
    _search_input = (By.ID, 'home-q')
    _expect_title = 'MDN Web Docs'
    _dev_tools_selector = (By.CSS_SELECTOR, '.home-features a[href$="en-US/docs/Tools"]')

    def confirm_page_load(self):
        assert self.selenium.title == self._expect_title

    def search(self, text):
        self.enter_text(self._search_input, text=text)
        self.send_key_press(key='ENTER')
        return SearchResultsPage(self.selenium, self.variables)

    def dev_tools(self):
        self.click(self._dev_tools_selector)
        return DevTools(self.selenium, self.variables)

