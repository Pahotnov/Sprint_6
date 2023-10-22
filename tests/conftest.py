import allure
import pytest
from selenium import webdriver
from urls import Urls


# Настройки драйвера
@allure.step('Открыть браузер Firefox. Удалить все куки. Перейти по ссылке https://qa-scooter.praktikum-services.ru/.')
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.delete_all_cookies()
    driver.get(Urls.YA_SCOOTER_MAIN_URL)

    yield driver
    driver.quit()
