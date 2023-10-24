import allure
import pytest

from data import Data
from pages.ya_scooter_main_page import YaScooterMainPage


class TestCheckAnswersOnQuestions:
    @allure.title('Проверка ответа на вопрос')
    @allure.description('Листаем вниз странцы до блока "Вопросы о важном". '
                        'Разворачиваем вопрос. '
                        'Проверяем текст ответа.')
    @pytest.mark.parametrize('question_locator, answer_locator, answer_text', Data.lists_of_questions_and_answers)
    def test_check_answers_on_questions(self, driver, question_locator, answer_locator, answer_text):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.click_on_question(question_locator)
        answer = ya_scooter_main_page.get_answer_text(answer_locator)
        assert answer == answer_text
