from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators


class OrderAltScooter(BaseLocators):
    BTN_NEXT = (By.XPATH, './/button[text()="Далее"]')
    BTN_SUBMIT_ORDER = (By.XPATH, './/button[contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]')
    BTN_CONFIRM_YES = (By.XPATH, './/button[text()="Да"]')
    BTN_VIEW_STATUS = (By.XPATH, './/button[text()="Посмотреть статус"]')
    INPUT_FIRST_NAME = (By.XPATH, './/input[@placeholder="* Имя"]')
    INPUT_LAST_NAME = (By.XPATH, './/input[@placeholder="* Фамилия"]')
    INPUT_ADDRESS = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
    INPUT_PHONE = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')
    INPUT_METRO = (By.XPATH, './/input[@placeholder="* Станция метро"]')
    METRO_DROPDOWN_PANEL = (By.XPATH, '//div[contains(@class, "select-search__select")]')
    INPUT_DELIVERY_DATE = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
    CALENDAR_SELECTED_DAY = (By.XPATH, './/div[contains(@class, "react-datepicker__day--selected")]')
    DROPDOWN_RENTAL_PERIOD = (By.CLASS_NAME, 'Dropdown-root')
    OPTION_RENTAL_3_DAYS = (By.XPATH, './/div[contains(@class, "Dropdown-option") and text()="трое суток"]')
    OPTION_RENTAL_4_DAYS = (By.XPATH, './/div[contains(@class, "Dropdown-option") and text()="четверо суток"]')
    CHECKBOX_COLOR_BLACK = (By.ID, 'black')
    CHECKBOX_COLOR_GREY = (By.ID, 'grey')
    INPUT_COURIER_COMMENT = (By.XPATH, './/input[@placeholder="Комментарий для курьера"]')