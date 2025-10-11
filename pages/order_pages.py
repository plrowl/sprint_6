from locators.order_locators import OrderAltScooter
from pages.base_pages import BasePage
import allure


class OrderPage(BasePage):
    def __init__(self, driver, time=10):
        super().__init__(driver, time)
        self.order_locators = OrderAltScooter

    @allure.step('Ввести станцию метро: {station}')
    def input_field_station(self, station: str):
        self.input_field(station, self.order_locators.INPUT_METRO)
        self.click_on_element(self.order_locators.METRO_DROPDOWN_PANEL)

    @allure.step('Получить локатор кнопки «Заказать»: {position}')
    def get_order_button(self, position: str):
        mapping = {
            'top': self.locators.BTN_ORDER_TOP,
            'bottom': self.locators.BTN_ORDER_BOTTOM,
        }
        return mapping.get(position)

    @allure.step('Проверить появление окна успешного заказа')
    def successful_rental(self) -> bool:
        return self.checking_the_window_with_a_successful_order(self.order_locators.BTN_VIEW_STATUS)

    @allure.step('Выбрать срок аренды: {period_label}')
    def select_period(self, period_label: str):
        mapping = {
            'трое суток': self.order_locators.OPTION_RENTAL_3_DAYS,
            'четверо суток': self.order_locators.OPTION_RENTAL_4_DAYS,
        }
        self.click_on_element(mapping[period_label])

    @allure.step('Выбрать цвет самоката: {color_key}')
    def select_color(self, color_key: str):
        mapping = {
            'black': self.order_locators.CHECKBOX_COLOR_BLACK,
            'grey':  self.order_locators.CHECKBOX_COLOR_GREY,
        }
        self.click_on_element(mapping[color_key])

    @allure.step('Заполнить форму «Личные данные»')
    def full_form_user(self, user_data: dict):
        with allure.step('Имя'):
            self.input_field(user_data['name'], self.order_locators.INPUT_FIRST_NAME)
        with allure.step('Фамилия'):
            self.input_field(user_data['surname'], self.order_locators.INPUT_LAST_NAME)
        with allure.step('Адрес'):
            self.fill_optional_field(user_data.get('address'), self.order_locators.INPUT_ADDRESS)
        with allure.step('Станция метро'):
            self.input_field_station(user_data['station'])
        with allure.step('Телефон'):
            self.input_field(user_data['phone'], self.order_locators.INPUT_PHONE)
        with allure.step('Далее'):
            self.click_on_element(self.order_locators.BTN_NEXT)

    @allure.step('Заполнить форму «Аренда самоката»')
    def full_form_rent(self, user_data: dict):
        with allure.step('Дата привоза'):
            self.input_field(user_data['date'], self.order_locators.INPUT_DELIVERY_DATE)
            self.click_on_element(self.order_locators.CALENDAR_SELECTED_DAY)
        with allure.step('Срок аренды'):
            self.click_on_element(self.order_locators.DROPDOWN_RENTAL_PERIOD)
            self.select_period(user_data['period_type'])
        with allure.step('Цвет самоката'):
            self.select_color(user_data['color_type'])
        with allure.step('Комментарий курьеру'):
            self.fill_optional_field(user_data.get('comment'), self.order_locators.INPUT_COURIER_COMMENT)
        with allure.step('Подтвердить заказ'):
            self.click_on_element(self.order_locators.BTN_SUBMIT_ORDER)
            self.click_on_element(self.order_locators.BTN_CONFIRM_YES)
