from pages.ya_scooter_main_page import YaScooterMainPage


class Data:
    FIRST_QUESTION_ANSWER = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    SECOND_QUESTION_ANSWER = 'Пока что у нас так: один заказ — один самокат. ' \
                             'Если хотите покататься с друзьями, ' \
                             'можете просто сделать несколько заказов — один за другим.'
    THIRD_QUESTION_ANSWER = 'Допустим, вы оформляете заказ на 8 мая. ' \
                            'Мы привозим самокат 8 мая в течение дня. ' \
                            'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. ' \
                            'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    FOURTH_QUESTION_ANSWER = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    FIFTH_QUESTION_ANSWER = 'Пока что нет! ' \
                            'Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    SIXTH_QUESTION_ANSWER = 'Самокат приезжает к вам с полной зарядкой. ' \
                            'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. ' \
                            'Зарядка не понадобится.'
    SEVENTH_QUESTION_ANSWER = 'Да, пока самокат не привезли. ' \
                              'Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    EIGHTH_QUESTION_ANSWER = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    SUCCESS_ORDER_TITLE = 'Заказ оформлен'

    lists_of_questions_and_answers = [
        [
            YaScooterMainPage.first_question, YaScooterMainPage.first_answer, FIRST_QUESTION_ANSWER
        ],
        [
            YaScooterMainPage.second_question, YaScooterMainPage.second_answer, SECOND_QUESTION_ANSWER
        ],
        [
            YaScooterMainPage.third_question, YaScooterMainPage.third_answer, THIRD_QUESTION_ANSWER
        ],
        [
            YaScooterMainPage.fourth_question, YaScooterMainPage.fourth_answer, FOURTH_QUESTION_ANSWER
        ],
        [
            YaScooterMainPage.fifth_question, YaScooterMainPage.fifth_answer, FIFTH_QUESTION_ANSWER
        ],
        [
            YaScooterMainPage.sixth_question, YaScooterMainPage.sixth_answer, SIXTH_QUESTION_ANSWER
        ],
        [
            YaScooterMainPage.seventh_question, YaScooterMainPage.seventh_answer, SEVENTH_QUESTION_ANSWER
        ],
        [
            YaScooterMainPage.eighth_question, YaScooterMainPage.eighth_answer, EIGHTH_QUESTION_ANSWER
        ],
    ]
