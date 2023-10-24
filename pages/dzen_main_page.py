from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DzenMainPage(BasePage):
    dzen_top_content_block = (By.CSS_SELECTOR, 'div[class*="dzen-wrapper-with-top-content-desktop__main"]')

    def get_dzen_main_page_url(self):
        self.find_element(self.dzen_top_content_block)
        return self.get_url()
