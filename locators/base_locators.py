from selenium.webdriver.common.by import By


class BaseLocators:
    LOGO_YANDEX = (By.XPATH, './/img[@alt="Yandex"]')
    LOGO_SCOOTER = (By.XPATH, './/img[@alt="Scooter"]')
    BTN_ORDER_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    BTN_ORDER_BOTTOM = (By.XPATH, './/button[contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]')
    FAQ_CONTAINER = (By.XPATH, "//div[contains(@class, 'Home_FAQ_')]")

    @staticmethod
    def FAQ_QUESTION(index: int):
        "Кнопка вопроса (заголовок аккордеона) по индексу 0..7"
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def FAQ_ANSWER(index: int):
        "Панель ответа аккордеона по индексу 0..7"
        return (By.ID, f"accordion__panel-{index}")