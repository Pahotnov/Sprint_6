import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DzenMainPage:
    dzen_top_content_block = (By.CSS_SELECTOR, 'div[class*="dzen-wrapper-with-top-content-desktop__main"]')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получить адрес текущей страницы')
    def get_url(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.dzen_top_content_block))
        return self.driver.current_url
