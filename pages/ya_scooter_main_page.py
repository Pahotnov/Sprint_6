from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class YaScooterMainPage:
    cookie_agreement = (By.ID, 'rcc-confirm-button')
    first_question = (By.XPATH, '//div[text()="Сколько это стоит? И как оплатить?"]')
    first_answer = (By.XPATH, '//div[text()="Сколько это стоит? И как оплатить?"]/following::p[1]')
    second_question = (By.XPATH, '//div[text()="Хочу сразу несколько самокатов! Так можно?"]')
    second_answer = (By.XPATH, '//div[text()="Хочу сразу несколько самокатов! Так можно?"]/following::p[1]')
    third_question = (By.XPATH, '//div[text()="Как рассчитывается время аренды?"]')
    third_answer = (By.XPATH, '//div[text()="Как рассчитывается время аренды?"]/following::p[1]')
    fourth_question = (By.XPATH, '//div[text()="Можно ли заказать самокат прямо на сегодня?"]')
    fourth_answer = (By.XPATH, '//div[text()="Можно ли заказать самокат прямо на сегодня?"]/following::p[1]')
    fifth_question = (By.XPATH, '//div[text()="Можно ли продлить заказ или вернуть самокат раньше?"]')
    fifth_answer = (By.XPATH, '//div[text()="Можно ли продлить заказ или вернуть самокат раньше?"]/following::p[1]')
    sixth_question = (By.XPATH, '//div[text()="Вы привозите зарядку вместе с самокатом?"]')
    sixth_answer = (By.XPATH, '//div[text()="Вы привозите зарядку вместе с самокатом?"]/following::p[1]')
    seventh_question = (By.XPATH, '//div[text()="Можно ли отменить заказ?"]')
    seventh_answer = (By.XPATH, '//div[text()="Можно ли отменить заказ?"]/following::p[1]')
    eighth_question = (By.XPATH, '//div[text()="Я жизу за МКАДом, привезёте?"]')
    eighth_answer = (By.XPATH, '//div[text()="Я жизу за МКАДом, привезёте?"]/following::p[1]')
    first_order_button = (By.XPATH, '(//button[text()="Заказать"])[1]')
    second_order_button = (By.XPATH, '(//button[text()="Заказать"])[2]')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликнуть на кнопку "да все привыкли"')
    def click_on_cookie_agreement(self):
        self.driver.find_element(*self.cookie_agreement).click()

    @allure.step('Кликнуть на вопрос в блоке "Вопросы о важном"')
    def click_on_question(self, question_locator):
        element = self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element(*question_locator).click()

    @allure.step('Дождаться раскрытия вопроса и вернуть текст ответа на него')
    def get_answer_text(self, answer_locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(answer_locator)).text

    @allure.step('Кликнуть на кнопку "Заказ"')
    def click_on_order_button(self, order_button_locator):
        element = self.driver.find_element(*order_button_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element(*order_button_locator).click()

    @allure.step('Получить адрес текущей страницы')
    def get_url(self):
        return self.driver.current_url
