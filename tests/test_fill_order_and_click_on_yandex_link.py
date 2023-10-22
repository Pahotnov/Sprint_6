import allure
import pytest

from helpers import get_name, get_surname, get_address, get_metro_station, get_phone_number, get_date, get_days_of_rent, get_color, get_comment
from pages.ya_scooter_main_page import YaScooterMainPage
from pages.ya_scooter_order_page import YaScooterOrderPage
from urls import Urls


class TestFillOrderAndClickOnYandexLink:
    @allure.title('Проверка ссылки "Яндекс"')
    @allure.description('Переходим по кнопкам "Заказ", заполняем все данные '
                        '(выбираются случайным образом из готовых наборов) и переходим по ссылке "Яндекс". '
                        'Переходим на открывшуюся вкладку. '
                        'Проверяем адрес текущей страницы.')
    @pytest.mark.parametrize('order_button', (YaScooterMainPage.first_order_button,
                                              YaScooterMainPage.second_order_button))
    def test_fill_order_and_click_on_yandex_link(self, driver, order_button):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.click_on_cookie_agreement()
        ya_scooter_main_page.click_on_order_button(order_button)
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.fill_name_field(get_name())
        ya_scooter_order_page.fill_surname_field(get_surname())
        ya_scooter_order_page.fill_address_field(get_address())
        ya_scooter_order_page.fill_metro_station_field(get_metro_station())
        ya_scooter_order_page.fill_phone_number_field(get_phone_number())
        ya_scooter_order_page.click_on_next_button()
        ya_scooter_order_page.choose_date(get_date())
        ya_scooter_order_page.choose_days_of_rent(get_days_of_rent())
        ya_scooter_order_page.choose_color(get_color())
        ya_scooter_order_page.fill_comment_for_courier(get_comment())
        dzen_main_page = ya_scooter_order_page.click_on_yandex_link()
        assert dzen_main_page.get_url() == Urls.DZEN_REDIRECT_MAIN_PAGE_URL
