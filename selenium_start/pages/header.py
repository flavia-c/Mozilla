from selenium.webdriver.common.by import By
from .basepage import BasePage
from .http import Http
from .ff_support import FfSupport

class Header(BasePage):

    _technologies_button_locator = (By.CSS_SELECTOR, '.nav-main-item > a[href$="/en-US/docs/Web"]')
    _http_button_locator = (By.CSS_SELECTOR, '#nav-tech-submenu a[href$="/docs/Web/HTTP"]')
    _feedback_button_locator = (By.CSS_SELECTOR, '.nav-main-item > a[href$="/en-US/docs/MDN/Feedback"]')
    _get_ff_help_locator = (By.CSS_SELECTOR, '#nav-contact-submenu a[href="https://support.mozilla.org/"]')

    def navigate_to_http_page(self):
        self.hover(self._technologies_button_locator)
        self.click(self._http_button_locator)

        return Http(self.selenium, self.variables)

    def navigate_to_ff_support_page(self):
        self.hover(self._feedback_button_locator)
        self.click(self._get_ff_help_locator)

        return FfSupport(self.selenium, self.variables)


