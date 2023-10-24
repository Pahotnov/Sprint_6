from selenium.webdriver.common.by import By
import allure

from pages.base_page import BasePage
from pages.dzen_main_page import DzenMainPage


class YaScooterMainPage(BasePage):
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
    scooter_link = (By.CSS_SELECTOR, 'img[alt="Scooter"]')
    yandex_link = (By.CSS_SELECTOR, 'img[alt="Yandex"]')

    @allure.step('Кликнуть на кнопку "да все привыкли"')
    def click_on_cookie_agreement(self):
        self.click_on(self.cookie_agreement)

    @allure.step('Кликнуть на вопрос в блоке "Вопросы о важном"')
    def click_on_question(self, question_locator):
        self.go_to_element(question_locator)
        self.click_on(question_locator)

    @allure.step('Дождаться раскрытия вопроса и вернуть текст ответа на него')
    def get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)

    @allure.step('Кликнуть на кнопку "Заказ"')
    def click_on_order_button(self, order_button_locator):
        self.go_to_element(order_button_locator)
        self.click_on(order_button_locator)

    @allure.step('Кликнуть на ссылку "Самокат"')
    def click_on_scooter_link(self):
        self.click_on(self.scooter_link)
        return YaScooterMainPage(self.driver)

    @allure.step('Кликнуть на ссылку "Яндекс" и перейти в открывшееся окно')
    def click_on_yandex_link(self):
        self.click_on(self.yandex_link)
        self.switch_to_window()
        return DzenMainPage(self.driver)
