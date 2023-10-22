import allure

from data import Data
from pages.ya_scooter_main_page import YaScooterMainPage


class TestCheckAnswersOnQuestions:
    @allure.title('Проверка ответа на первый вопрос')
    @allure.description('Листаем вниз странцы до блока "Вопросы о важном". '
                        'Разворачиваем первый вопрос. '
                        'Проверяем текст ответа.')
    def test_check_answer_on_first_question(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.click_on_question(YaScooterMainPage.first_question)
        answer = ya_scooter_main_page.get_answer_text(YaScooterMainPage.first_answer)
        assert answer == Data.FIRST_QUESTION_ANSWER

    @allure.title('Проверка ответа на второй вопрос')
    @allure.description('Листаем вниз странцы до блока "Вопросы о важном". '
                        'Разворачиваем второй вопрос. '
                        'Проверяем текст ответа.')
    def test_check_answer_on_second_question(self, driver):
        ya_main_page = YaScooterMainPage(driver)
        ya_main_page.click_on_question(YaScooterMainPage.second_question)
        answer = ya_main_page.get_answer_text(YaScooterMainPage.second_answer)
        assert answer == Data.SECOND_QUESTION_ANSWER

    @allure.title('Проверка ответа на третий вопрос')
    @allure.description('Листаем вниз странцы до блока "Вопросы о важном". '
                        'Разворачиваем третий вопрос. '
                        'Проверяем текст ответа.')
    def test_check_answer_on_third_question(self, driver):
        ya_main_page = YaScooterMainPage(driver)
        ya_main_page.click_on_question(YaScooterMainPage.third_question)
        answer = ya_main_page.get_answer_text(YaScooterMainPage.third_answer)
        assert answer == Data.THIRD_QUESTION_ANSWER

    @allure.title('Проверка ответа на четвёртый вопрос')
    @allure.description('Листаем вниз странцы до блока "Вопросы о важном". '
                        'Разворачиваем четвёртый вопрос. '
                        'Проверяем текст ответа.')
    def test_check_answer_on_fourth_question(self, driver):
        ya_main_page = YaScooterMainPage(driver)
        ya_main_page.click_on_question(YaScooterMainPage.fourth_question)
        answer = ya_main_page.get_answer_text(YaScooterMainPage.fourth_answer)
        assert answer == Data.FOURTH_QUESTION_ANSWER

    @allure.title('Проверка ответа на пятый вопрос')
    @allure.description('Листаем вниз странцы до блока "Вопросы о важном". '
                        'Разворачиваем пятый вопрос. '
                        'Проверяем текст ответа.')
    def test_check_answer_on_fifth_question(self, driver):
        ya_main_page = YaScooterMainPage(driver)
        ya_main_page.click_on_question(YaScooterMainPage.fifth_question)
        answer = ya_main_page.get_answer_text(YaScooterMainPage.fifth_answer)
        assert answer == Data.FIFTH_QUESTION_ANSWER

    @allure.title('Проверка ответа на шестой вопрос')
    @allure.description('Листаем вниз странцы до блока "Вопросы о важном". '
                        'Разворачиваем шестой вопрос. '
                        'Проверяем текст ответа.')
    def test_check_answer_on_sixth_question(self, driver):
        ya_main_page = YaScooterMainPage(driver)
        ya_main_page.click_on_question(YaScooterMainPage.sixth_question)
        answer = ya_main_page.get_answer_text(YaScooterMainPage.sixth_answer)
        assert answer == Data.SIXTH_QUESTION_ANSWER

    @allure.title('Проверка ответа на седьмой вопрос')
    @allure.description('Листаем вниз странцы до блока "Вопросы о важном". '
                        'Разворачиваем седьмой вопрос. '
                        'Проверяем текст ответа.')
    def test_check_answer_on_seventh_question(self, driver):
        ya_main_page = YaScooterMainPage(driver)
        ya_main_page.click_on_question(YaScooterMainPage.seventh_question)
        answer = ya_main_page.get_answer_text(YaScooterMainPage.seventh_answer)
        assert answer == Data.SEVENTH_QUESTION_ANSWER

    @allure.title('Проверка ответа на восьмой вопрос')
    @allure.description('Листаем вниз странцы до блока "Вопросы о важном". '
                        'Разворачиваем восьмой вопрос. '
                        'Проверяем текст ответа.')
    def test_check_answer_on_eighth_question(self, driver):
        ya_main_page = YaScooterMainPage(driver)
        ya_main_page.click_on_question(YaScooterMainPage.eighth_question)
        answer = ya_main_page.get_answer_text(YaScooterMainPage.eighth_answer)
        assert answer == Data.EIGHTH_QUESTION_ANSWER
