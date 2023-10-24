from selenium.webdriver.common.by import By
import allure

from pages.base_page import BasePage


class YaScooterOrderPage(BasePage):
    name_input = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    surname_input = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    address_input = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    metro_station_input = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
    metro_station_name = (By.XPATH, './/div[text()="{metro_station}"]')
    phone_number_input = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
    next_button = (By.CSS_SELECTOR, 'button[class*="Button_Middle"]')
    datepicker_input = (By.CSS_SELECTOR, 'div[class*="react-datepicker__input-container"]')
    datepicker_date = (By.XPATH, '//div[text()="{day}"]')
    rent_dropdown = (By.CSS_SELECTOR, 'div[class*="Dropdown-root"]')
    count_of_days = (By.XPATH, '(//div[@class="Dropdown-option"])[{count}]')
    scooter_color = (By.ID, '{color}')
    comment_for_courier_input = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')
    create_order_button = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]')
    yes_order_button = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Да"]')
    order_created_success_modal_window = (By.XPATH, '//div[text()="Заказ оформлен"]')

    @allure.step('Заполнить поле "Имя"')
    def fill_name_field(self, name):
        self.fill_field(self.name_input, name)

    @allure.step('Заполнить поле "Фамилия"')
    def fill_surname_field(self, surname):
        self.fill_field(self.surname_input, surname)

    @allure.step('Заполнить поле "Адрес"')
    def fill_address_field(self, address):
        self.fill_field(self.address_input, address)

    @allure.step('Ввести название станции метро и выбрать её в выпадающем списке "Станция метро"')
    def fill_metro_station_field(self, metro_station):
        self.fill_field(self.metro_station_input, metro_station)
        metro_station_name = (By.XPATH, f'.//div[text()="{metro_station}"]')
        self.click_on(metro_station_name)

    @allure.step('Заполнить поле "Номер телефона"')
    def fill_phone_number_field(self, phone_number):
        self.fill_field(self.phone_number_input, phone_number)

    @allure.step('Нажать на кнопку "Далее')
    def click_on_next_button(self):
        self.click_on(self.next_button)

    @allure.step('Выбрать дату в дейтпикере')
    def choose_date(self, day):
        self.click_on(self.datepicker_input)
        datepicker_date = (By.XPATH, f'//div[text()="{day}"]')
        self.click_on(datepicker_date)

    @allure.step('Выбрать количество дней аренды в выпадающем списке "Срок аренды"')
    def choose_days_of_rent(self, count):
        self.click_on(self.rent_dropdown)
        count_of_days = (By.XPATH, f'(//div[@class="Dropdown-option"])[{count}]')
        self.click_on(count_of_days)

    @allure.step('Выбрать цвет в поле "Цвет самоката"')
    def choose_color(self, color):
        scooter_color = (By.ID, f'{color}')
        self.click_on(scooter_color)

    @allure.step('Заполнить поле "Комментарий для курьера"')
    def fill_comment_for_courier(self, comment):
        self.fill_field(self.comment_for_courier_input, comment)

    @allure.step('Нажать на кнопку "Заказать" под формой "Про аренду"')
    def click_on_create_order_button(self):
        self.click_on(self.create_order_button)

    @allure.step('Нажать на кнопку "Да" в модальном окне "Хотите оформить заказ?"')
    def click_on_yes_order_button(self):
        self.click_on(self.yes_order_button)

    @allure.step('Дождаться появления модального окна "Ваш заказ оформлен" и вернуть из него текст')
    def modal_window_of_success_order_is_on_page(self):
        return self.get_text(self.order_created_success_modal_window)
