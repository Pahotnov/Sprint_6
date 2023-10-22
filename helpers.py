from random import randint


def get_name():
    list_of_addresses = ['Артемий', 'Елена', 'Василий', 'Михаил', 'Светлана']
    return list_of_addresses[randint(0, 4)]


def get_surname():
    list_of_addresses = ['Долгопрудов', 'Пупкин', 'Фамилия', 'Прокопова', 'Шакша']
    return list_of_addresses[randint(0, 4)]


def get_address():
    list_of_addresses = ['Владивосток', 'Москва', 'Краснодар', 'Санкт-Петербург', 'Красногвардейск']
    return list_of_addresses[randint(0, 4)]


def get_metro_station():
    list_of_metro_stations = ['Черкизовская', 'Сокол', 'Молодёжная', 'Фили', 'ВДНХ', 'Спартак',
                              'Минская', 'Бибирево', 'Трубная', 'Каховская', 'Лесопарковая', 'Деловой центр']
    return list_of_metro_stations[randint(0, 11)]


def get_phone_number():
    phone_number = ''
    for i in range(0, 11):
        phone_number = phone_number + str(randint(0, 9))
    return phone_number


def get_date():
    return randint(10, 20)


def get_days_of_rent():
    return randint(1, 7)


def get_color():
    list_of_colors = ['grey', 'black']
    return list_of_colors[randint(0, 1)]


def get_comment():
    list_of_comments = ['Тест', 'Комментарий', 'Привет, хотел бы оставить комментарий для тебя', 12345,
                        'Дайте мне 50 самокатов']
    return list_of_comments[randint(0, 4)]
