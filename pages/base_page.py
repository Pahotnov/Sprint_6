from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))

    def get_url(self):
        return self.driver.current_url

    def go_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def click_on(self, locator):
        self.find_element(locator).click()

    def fill_field(self, locator, data):
        self.find_element(locator).send_keys(data)

    def get_text(self, locator):
        return self.find_element(locator).text
