from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_locators import BaseLocators
from url import Url
import allure
from data import Data


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.driver.get(Url.url_page)
        self.locators = BaseLocators


    @allure.step("Переключиться на последнюю вкладку")
    def go_to_the_last_tab(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

    @allure.step("Ждать видимости элемента")
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ждать кликабельности элемента")
    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть по элементу")
    def click_on_element(self, locator):
        self.wait_for_element_clickable(locator).click()

    @allure.step("Ввести текст в поле")
    def input_field(self, text, locator):
        field = self.wait_for_element_clickable(locator)
        field.click()
        field.send_keys(text)

    @allure.step("Заполнить необязательное поле")
    def fill_optional_field(self, text, locator):
        if text is not None:
            self.input_field(text, locator)

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        return self.wait_for_element_visible(locator).text

    @allure.step('Получить атрибут "{attribute_name}" элемента')
    def get_element_attribute(self, locator, attribute_name):
        return self.wait_for_element_visible(locator).get_attribute(attribute_name)

    @allure.step("Дождаться точного URL: {url}")
    def wait_url(self, url):
        return self.wait.until(lambda d: d.current_url == url)

    @allure.step("Получить текущий URL")
    def return_url(self):
        return self.driver.current_url

    @allure.step("Проверить, что элемент отображается")
    def checking_the_window_with_a_successful_order(self, locator):
        return self.wait_for_element_visible(locator).is_displayed()


    @allure.step('Кликнуть верхнюю кнопку «Заказать»')
    def click_order_button_top(self):
        self.click_on_element(self.locators.BTN_ORDER_TOP)

    @allure.step('Кликнуть нижнюю кнопку «Заказать»')
    def click_order_button_bottom(self):
        self.click_on_element(self.locators.BTN_ORDER_BOTTOM)


    @allure.step("Кликнуть по вопросу FAQ #{index}")
    def click_faq_question(self, index: int):
        self.scroll_to_element(self.locators.FAQ_CONTAINER)
        self.click_on_element(self.locators.FAQ_QUESTION(index))

    @allure.step("Получить текст ответа FAQ #{index}")
    def get_faq_answer_text(self, index: int):
        answer = self.wait_for_element_visible(self.locators.FAQ_ANSWER(index))
        return answer.text


    @allure.step("Получить ожидаемый текст FAQ #{index} из Data.list_text")
    def get_expected_text(self, index: int):
        return Data.list_text[index]
