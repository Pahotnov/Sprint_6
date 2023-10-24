# Это дубль теста test_first_order.py, так как в задании сказано,
# что необходимо проверить кнопки "Заказ" с минимум двумя наборами данных.
import allure
import pytest

from data import Data
from helpers import get_name, get_surname, get_address, get_metro_station, get_phone_number, get_date, get_days_of_rent, get_color, get_comment
from pages.ya_scooter_main_page import YaScooterMainPage
from pages.ya_scooter_order_page import YaScooterOrderPage


class TestFirstOrder:
    @allure.title('Проверка второго заказа')
    @allure.description('Переходим по кнопкам "Заказ", заполняем все данные '
                        '(выбираются случайным образом из готовых наборов) и создаём заказ. '
                        'Проверяем наличие модального окна с заголовком "Заказ оформлен".')
    @pytest.mark.parametrize('order_button', (YaScooterMainPage.first_order_button,
                                              YaScooterMainPage.second_order_button))
    def test_second_order(self, driver, order_button):
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
        ya_scooter_order_page.click_on_create_order_button()
        ya_scooter_order_page.click_on_yes_order_button()
        modal_window = ya_scooter_order_page.modal_window_of_success_order_is_on_page()
        assert Data.SUCCESS_ORDER_TITLE in modal_window
