from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

from pages.dzen_main_page import DzenMainPage
from pages.ya_scooter_main_page import YaScooterMainPage


class YaScooterOrderPage:
    name_input = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    surname_input = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    address_input = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    metro_station_input = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
    phone_number_input = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
    next_button = (By.CSS_SELECTOR, 'button[class*="Button_Middle"]')
    datepicker_input = (By.CSS_SELECTOR, 'div[class*="react-datepicker__input-container"]')
    rent_dropdown = (By.CSS_SELECTOR, 'div[class*="Dropdown-root"]')
    comment_for_courier_input = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')
    create_order_button = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]')
    yes_order_button = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Да"]')
    order_created_success_modal_window = (By.XPATH, '//div[text()="Заказ оформлен"]')
    scooter_link = (By.CSS_SELECTOR, 'img[alt="Scooter"]')
    yandex_link = (By.CSS_SELECTOR, 'img[alt="Yandex"]')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполнить поле "Имя"')
    def fill_name_field(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    @allure.step('Заполнить поле "Фамилия"')
    def fill_surname_field(self, surname):
        self.driver.find_element(*self.surname_input).send_keys(surname)

    @allure.step('Заполнить поле "Адрес"')
    def fill_address_field(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)

    @allure.step('Ввести название станции метро и выбрать её в выпадающем списке "Станция метро"')
    def fill_metro_station_field(self, metro_station):
        self.driver.find_element(*self.metro_station_input).send_keys(metro_station)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located
                                            ((By.XPATH, f'.//div[text()="{metro_station}"]')))  # Решил вынести локатор сюда для универсальности метода
        self.driver.find_element(By.XPATH, f'.//div[text()="{metro_station}"]').click()  # Решил вынести локатор сюда для универсальности метода

    @allure.step('Заполнить поле "Номер телефона"')
    def fill_phone_number_field(self, phone_number):
        self.driver.find_element(*self.phone_number_input).send_keys(phone_number)

    @allure.step('Нажать на кнопку "Далее')
    def click_on_next_button(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step('Выбрать дату в дейтпикере')
    def choose_date(self, day):
        self.driver.find_element(*self.datepicker_input).click()
        self.driver.find_element(By.XPATH, f'//div[text()="{day}"]').click()  # Решил вынести локатор сюда для универсальности метода

    @allure.step('Выбрать количество дней аренды в выпадающем списке "Срок аренды"')
    def choose_days_of_rent(self, count_of_days):
        self.driver.find_element(*self.rent_dropdown).click()
        self.driver.find_element(By.XPATH, f'(//div[@class="Dropdown-option"])[{count_of_days}]').click()  # Решил вынести локатор сюда для универсальности метода

    @allure.step('Выбрать цвет в поле "Цвет самоката"')
    def choose_color(self, color):
        self.driver.find_element(By.ID, f'{color}').click()  # Решил вынести локатор сюда для универсальности метода

    @allure.step('Заполнить поле "Комментарий для курьера"')
    def fill_comment_for_courier(self, comment):
        self.driver.find_element(*self.comment_for_courier_input).send_keys(comment)

    @allure.step('Нажать на кнопку "Заказать" под формой "Про аренду"')
    def click_on_create_order_button(self):
        self.driver.find_element(*self.create_order_button).click()

    @allure.step('Нажать на кнопку "Да" в модальном окне "Хотите оформить заказ?"')
    def click_on_yes_order_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.
                                             visibility_of_element_located(self.yes_order_button)).click()

    @allure.step('Дождаться появления модального окна "Ваш заказ оформлен" и вернуть из него текст')
    def modal_window_of_success_order_is_on_page(self):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located
                                                    (self.order_created_success_modal_window)).text

    @allure.step('Кликнуть на ссылку "Самокат"')
    def click_on_scooter_link(self):
        self.driver.find_element(*self.scooter_link).click()
        return YaScooterMainPage(self.driver)

    @allure.step('Кликнуть на ссылку "Яндекс" и перейти в открывшееся окно')
    def click_on_yandex_link(self):
        self.driver.find_element(*self.yandex_link).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return DzenMainPage(self.driver)
