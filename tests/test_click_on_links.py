import allure

from pages.ya_scooter_main_page import YaScooterMainPage
from urls import Urls


class TestClickOnLinks:
    @allure.title('Проверка ссылки "Яндекс"')
    @allure.description('Переходим по ссылке "Яндекс". '
                        'Переходим на открывшуюся вкладку. '
                        'Проверяем адрес текущей страницы.')
    def test_click_on_yandex_link(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        dzen_main_page = ya_scooter_main_page.click_on_yandex_link()
        assert dzen_main_page.get_dzen_main_page_url() == Urls.DZEN_REDIRECT_MAIN_PAGE_URL

    @allure.title('Проверка ссылки "Самокат"')
    @allure.description('Переходим по ссылке "Самокат". '
                        'Проверяем адрес текущей страницы.')
    def test_click_on_scooter_link(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page = ya_scooter_main_page.click_on_scooter_link()
        assert ya_scooter_main_page.get_url() == Urls.YA_SCOOTER_MAIN_URL
